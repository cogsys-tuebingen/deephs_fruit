import pytorch_lightning as lightning
from pytorch_lightning.loggers.wandb import WandbLogger
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.callbacks import ModelCheckpoint
import torch
import numpy as np
from torchvision import transforms
import argparse
import random
from torch.utils.data import DataLoader

from core.run_utils import get_current_git_hash
from core.name_convention import *
import core.argparser_utils as argparser_utils
from core.loss.focalloss import FocalLoss
from core.optimizer.adabound import AdaBound
from core.hyperspectral_dataset import HyperspectralDataset, get_records
from classification.transformers.to_rgb import ToRGB, NormalizeRGB
from classification.transformers.to_pca import DecompisiteWithPCA
from classification.transformers.normalize import Normalize
from classification.models import *
from classification.transformers.data_augmentation import Augmenter, AUGMENTATION_CONFIG
from classification.utils.confusion_matrix import log_confusion_matrix
from core.lightning_callbacks.lr_logger import LRLoggingCallback


def get_model(hparams):
    if hparams['reduction'] == 'rgb':
        bands = 3
    elif hparams['reduction'] == 'pca':
        bands = 5
    else:
        bands = hparams['bands']

    if hparams['model'] == 'ours':
        model = ClassifierNetwork(bands)
    elif hparams['model'] == 'resnet':
        model = resnet18(False, bands=bands, num_classes=3)
    elif hparams['model'] == 'alexnet':
        model = AlexNet(bands=bands, num_classes=3)
    else:
        raise Exception("Model %s is not in known models (ours, resnet)" % hparams['model'])

    return model


class DeepHsModule(lightning.LightningModule):
    def __init__(self, hparams):
        super(DeepHsModule, self).__init__()
        self._estimator_type = 'classifier'

        self.hparams = hparams

        self.model = get_model(hparams)
        self.critertion = FocalLoss(size_average=False)

    def setup(self, stage: str):
        self.train_records, self.val_records, self.test_records = \
            get_records(self.hparams['fruit'],
                        self.hparams['camera_type'],
                        self.hparams['classification_type'],
                        use_inter_ripeness_levels=self.hparams['use_inter_ripeness_levels'],
                        extend_unripe=self.hparams['extend_unripe']
                                      and self.hparams['classification_type'] == ClassificationType.RIPENESS,
                        )

        preprocessing = []
        if self.hparams['reduction'] == 'rgb':
            preprocessing.append(ToRGB(self.hparams['camera_type']))
            preprocessing.append(NormalizeRGB())
        elif self.hparams['reduction'] == 'pca':
            preprocessing.append(DecompisiteWithPCA(self.hparams['camera_type'], self.hparams['fruit']))
        else:
            preprocessing.append(Normalize(self.hparams['camera_type']))

        if stage == 'fit':
            self.train_dataset = HyperspectralDataset(self.hparams['classification_type'], self.train_records,
                                                      data_path=self.hparams['data_path'], balance_to=0,
                                                      transform=transforms.Compose(
                                                          [Augmenter(self.hparams['classification_type'],
                                                                     augmentation_config=
                                                                     self.hparams['augmentation_config'])]
                                                          + preprocessing),
                                                      input_size=(64, 64))
            self.val_dataset = HyperspectralDataset(self.hparams['classification_type'],
                                                    self.val_records,
                                                    data_path=self.hparams['data_path'], balance_to=None,
                                                    transform=transforms.Compose(preprocessing),
                                                    input_size=(64, 64))
        elif stage == 'test':
            self.test_dataset = HyperspectralDataset(self.hparams['classification_type'], self.test_records,
                                                     data_path=self.hparams['data_path'], balance_to=None,
                                                     transform=transforms.Compose(preprocessing),
                                                     input_size=(64, 64))

    def train_dataloader(self) -> DataLoader:
        return DataLoader(self.train_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'],
                          shuffle=True, drop_last=True)

    def val_dataloader(self) -> DataLoader:
        return DataLoader(self.val_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'],
                          shuffle=False)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'])

    def forward(self, x, test_augmentation=True):
        if test_augmentation:
            augmenter = Augmenter(self.hparams['classification_type'],
                                  augmentation_config=
                                  self.hparams['augmentation_config'])

            iterations = 5

            preds = torch.zeros((iterations, len(x), 3))

            for i in range(iterations):
                # the augmentation should not change the label, so we can ignore it here.
                _batch = [augmenter((_x, _y)) for _x, _y in zip(x.clone(), torch.zeros((x.shape[0], 1)))]
                _x = torch.stack(list(zip(*_batch))[0])

                preds[i] = self.model(_x)

            pred = preds.mean(0)
        else:
            pred = self.model(x)

        return pred

    @torch.no_grad()
    def predict(self, x, test_augmentation=True):
        return self.forward(x.cuda(), test_augmentation=test_augmentation).argmax(-1).detach().cpu()

    def training_step(self, batch, batch_id):
        x, y = batch

        pred = self.model(x)
        loss = self.critertion(pred, y)

        accuracy = ((pred.argmax(1) == y).sum().float() / x.shape[0]).detach()

        return {
            'loss': loss,
            'log': {
                'train/loss': loss,
                'train/accuracy': accuracy
            },
            'progress_bar': {
                'accuracy': accuracy
            }
        }

    def validation_step(self, batch, batch_id):
        x, y = batch

        pred = self.model(x)
        loss = self.critertion(pred, y)

        accuracy = ((pred.argmax(1) == y).sum().float() / x.shape[0]).detach()

        return {
            'val_loss': loss,
            'val_accuracy': accuracy,
            'log': {
                'val/loss': loss,
                'val/accuracy': accuracy
            }
        }

    def validation_epoch_end(self, outputs):
        val_accuracy = torch.stack([o['val_accuracy'] for o in outputs]).mean()
        val_loss = torch.stack([o['val_loss'] for o in outputs]).mean()

        return {
            'val_loss': val_loss,
            'val_accuracy': val_accuracy,
            'log': {
                'val/loss': val_loss,
                'val/accuracy': val_accuracy
            },
            'progress_bar': {
                'val_accuracy': val_accuracy,
                'val_loss': val_loss
            }
        }

    def test_step(self, batch, batch_id):
        x, y = batch

        pred = self.forward(x,
                            test_augmentation=self.hparams['test_augmentation'])
        pred = pred.to(y.device)
        loss = self.critertion(pred, y)
        accuracy = ((pred.argmax(1) == y).sum().float() / x.shape[0]).detach()

        return {
            'test_loss': loss,
            'test_accuracy': accuracy,
            'test_ys': torch.stack([torch.tensor([y_pred, y_true]) for y_pred, y_true in zip(pred.argmax(1), y)])
        }

    def test_epoch_end(self, outputs):
        test_accuracy = torch.stack([o['test_accuracy'] for o in outputs]).mean()
        test_loss = torch.stack([o['test_loss'] for o in outputs]).mean()
        test_ys = torch.cat([o['test_ys'] for o in outputs])

        self.logger.experiment.summary['test_accuracy'] = test_accuracy
        self.logger.experiment.summary['test_loss'] = test_loss

        labels = []
        if self.hparams['classification_type'] == ClassificationType.RIPENESS:
            labels = ["Unripe", "Ripe", "Overripe"]
        elif self.hparams['classification_type'] == ClassificationType.FIRMNESS:
            labels = ["Too hard", "Perfect", "Too soft"]
        elif self.hparams['classification_type'] == ClassificationType.SUGAR:
            labels = ["Not sweet", "Perfect", "Too sweet"]

        log_confusion_matrix(self.logger, test_ys[:, 0], test_ys[:, 1], labels=labels)

        return {
            'log':
                {
                    'test_loss': test_loss,
                    'test_accuracy': test_accuracy,
                }
        }

    def configure_optimizers(self):
        self.optimizer = AdaBound(self.model.parameters(), lr=self.hparams['lr'])
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, verbose=True)

        return {
            'optimizer': self.optimizer,
            'lr_scheduler': self.scheduler,
            'monitor': 'val_loss'
        }


def get_args():
    parser = argparse.ArgumentParser(
        "DeepHS:")
    parser.add_argument("--batch_size", type=int, default=32, help="The number of images per batch")
    parser.add_argument("--lr", type=float, default=1e-2)
    parser.add_argument('--fruit', type=argparser_utils.str2fruit, default=Fruit.AVOCADO)
    parser.add_argument('--camera_type', type=argparser_utils.str2cameratype, default=CameraType.VIS)
    parser.add_argument('--classification_type', type=argparser_utils.str2classification_type,
                        default=ClassificationType.FIRMNESS)
    parser.add_argument("--num_epochs", type=int, default=5000)
    parser.add_argument("--data_path", type=str, required=True, help="the root folder of dataset")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--log_path", type=str, default=None)
    parser.add_argument("--online_logging", default=False, action='store_true')

    parser.add_argument("--reduction", default=None, type=str, help='None, "rgb" or "pca"')
    parser.add_argument("--model", default="ours", type=str)

    # Extend data
    parser.add_argument("--extend_unripe", default=False, type=bool,
                        help="Define all records previous to a unripe label as unripe too")
    parser.add_argument("--use_inter_ripeness_levels", default=True, type=bool,
                        help="Use the inter ripeness levels")

    args = parser.parse_args()

    if args.reduction not in [None, 'rgb', 'pca']:
        raise Exception("Invalid value for reduction")

    return args


if __name__ == "__main__":
    opt = get_args()
    num_gpus = torch.cuda.device_count()

    # fix the seed for reproducibility
    seed = opt.seed
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)

    hparams = vars(opt)
    hparams['git_id'] = get_current_git_hash()
    hparams['batch_size'] = opt.batch_size
    hparams['num_workers'] = 8

    hparams['bands'] = len(util.get_wavelengths_for(opt.camera_type))
    hparams['augmentation_config'] = AUGMENTATION_CONFIG
    # hparams['augmentation_config']['random_noise'] = False
    # hparams['augmentation_config']['random_cut'] = False
    hparams['test_augmentation'] = True

    print("Hparams: %s" % hparams)

    model = DeepHsModule(hparams)
    logger = WandbLogger(hparams['git_id'], offline=not opt.online_logging,
                         save_dir=opt.log_path, project='deephs')

    early_stop_callback = EarlyStopping(
        monitor='val_loss',
        min_delta=0.00,
        verbose=True,
        mode='min',
        patience=20
    )

    checkpoint_callback = ModelCheckpoint(
        filepath='best.ckpt',
        save_top_k=1,
        verbose=True,
        monitor='val_loss',
        mode='min'
    )

    trainer = lightning.Trainer(max_epochs=opt.num_epochs, gpus=-1, logger=logger,
                                early_stop_callback=early_stop_callback, min_epochs=50,
                                checkpoint_callback=checkpoint_callback, callbacks=[LRLoggingCallback()])

    trainer.fit(model)
    best_model = DeepHsModule.load_from_checkpoint(checkpoint_callback.best_model_path)

    print("Best model..")
    trainer.test(best_model)
