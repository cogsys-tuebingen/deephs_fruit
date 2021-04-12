import tqdm
import matplotlib.pyplot as plt
from core.fruit_list import *
from false_color_images.autoencoder import AutoencoderModel
from false_color_images.classifier import ClassifierModel

import pytorch_lightning as lightning
from pytorch_lightning.loggers.wandb import WandbLogger
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.callbacks import ModelCheckpoint
import torch
import argparse
import random
from torch.utils.data import DataLoader

from core.run_utils import get_current_git_hash

from core.name_convention import *
import core.argparser_utils as argparser_utils
from core.loss.focalloss import FocalLoss

from core.hyperspectral_dataset import get_records
from classification.train import DeepHsModule
from classification.transformers.data_augmentation import AUGMENTATION_CONFIG
from classification.transformers.normalize import Normalize
from core.optimizer.adabound import AdaBound


def extract_pixels(path, fruit: FruitRecord):
    _envi_header, _envi_data = fruit.load(path, True)
    _pixels = _envi_data.reshape(-1, _envi_data.shape[2])

    return _pixels


def get_records(all_records, path, camera_type):
    all_pixels = np.zeros((0, len(util.get_wavelengths_for(camera_type))))

    for record in tqdm.tqdm(all_records, "Extract pixels of records"):
        pixels = extract_pixels(path, record)

        if pixels is not None:
            all_pixels = np.append(all_pixels, pixels, axis=0)

    print("# Load pixels %i" % len(all_pixels))

    pixel_count = len(all_pixels)
    train_set_size = int(float(pixel_count) * 15 / 16)
    idx_train = np.random.choice(list(range(pixel_count)), train_set_size, replace=False)
    train_set_mask = np.zeros(pixel_count, dtype=bool)
    train_set_mask[idx_train] = True
    train_set = torch.from_numpy(all_pixels[train_set_mask]).float()
    val_set = torch.from_numpy(all_pixels[np.logical_not(train_set_mask)]).float()

    print("# Train set size %i" % len(train_set))
    print("# Val set size %i" % len(val_set))

    return train_set, val_set


class PixelwiseNormalize(Normalize):
    def __init__(self, camera_type: CameraType):
        super(PixelwiseNormalize, self).__init__(camera_type)

    def __call__(self, pixel):

        pixel = ((pixel.numpy() - self.mean) / self.std)

        return torch.from_numpy(pixel).float()


class FalseColorAutoencoderModule(lightning.LightningModule):
    def __init__(self, hparams, all_records):
        super(FalseColorAutoencoderModule, self).__init__()

        self.hparams = hparams

        self.model = AutoencoderModel(hparams['bands'])
        self.critertion = torch.nn.MSELoss()

        self.all_records = all_records

    def setup(self, stage: str):
        self.train_dataset, self.val_dataset = get_records(self.all_records, self.hparams['data_path'],
                                                           self.hparams['camera_type'])

        normalizer = PixelwiseNormalize(self.hparams['camera_type'])

        self.train_dataset = [normalizer(p) for p in self.train_dataset]
        self.val_dataset = [normalizer(p) for p in self.val_dataset]


    def train_dataloader(self) -> DataLoader:
        return DataLoader(self.train_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'],
                          shuffle=True, drop_last=True)

    def val_dataloader(self) -> DataLoader:
        return DataLoader(self.val_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'],
                          shuffle=False)

    def forward(self, x):
        return self.model(x)

    def encode(self, x):
        return self.model.encode(x)

    def decode(self, x):
        return self.model.decode(x)

    def training_step(self, batch, batch_id):
        x = batch

        pred = self.model(x)
        loss = self.critertion(pred, x)

        return {
            'loss': loss,
            'log': {
                'train/loss': loss,
            }
        }

    def validation_step(self, batch, batch_id):
        x = batch

        pred = self.model(x)
        loss = self.critertion(pred, x)

        return {
            'val_loss': loss,
            'log': {
                'val/loss': loss,
            }
        }

    def validation_epoch_end(self, outputs):
        val_loss = torch.stack([o['val_loss'] for o in outputs]).mean()

        return {
            'val_loss': val_loss,
            'log': {
                'val/loss': val_loss,
            },
        }

    def configure_optimizers(self):
        self.optimizer = torch.optim.Adam(self.model.parameters(),
                                          lr=self.hparams['lr'])
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, verbose=True,
                                                                    patience=2, threshold=1e-2)

        return {
            'optimizer': self.optimizer,
            'lr_scheduler': self.scheduler,
            'monitor': 'val_loss'
        }


class FalseColorClassifierModule(DeepHsModule):
    def __init__(self, hparams, autoencoder: AutoencoderModel):
        hparams['batch_size'] = 64
        hparams['lr'] = 1e-4
        hparams['augmentation_config'] = AUGMENTATION_CONFIG
        hparams['reduction'] = None
        hparams['model'] = 'ours'
        super(FalseColorClassifierModule, self).__init__(hparams)
        self._estimator_type = 'classifier'

        self.hparams = hparams

        self.model = ClassifierModel(autoencoder, hparams['bands'])
        self.critertion = FocalLoss()

def get_args():
    parser = argparse.ArgumentParser(
        "DeepHS PreTrained:")
    parser.add_argument('--classification_type', type=argparser_utils.str2classification_type,
                        default=ClassificationType.FIRMNESS)
    parser.add_argument("--batch_size", type=int, default=10000, help="The number of images per batch")
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument('--fruit', type=argparser_utils.str2fruit, default=Fruit.AVOCADO)
    parser.add_argument('--camera_type', type=argparser_utils.str2cameratype, default=CameraType.VIS)
    parser.add_argument("--num_epochs", type=int, default=100)
    parser.add_argument("--data_path", type=str, default="", help="the root folder of dataset")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--log_path", type=str, default=None)
    parser.add_argument("--online_logging", default=False, action='store_true')

    # Extend data
    parser.add_argument("--extend_unripe", default=True, type=bool,
                        help="Define all records previous to a unripe label as unripe too")
    parser.add_argument("--use_inter_ripeness_levels", default=True, type=bool,
                        help="Use the inter ripeness levels")
    args = parser.parse_args()
    return args


def plot_encoded_img(autoencoder, r: FruitRecord):
    autoencoder = autoencoder.to('cuda')
    normalizer = PixelwiseNormalize(opt.camera_type)

    l = r.load(opt.data_path, True)[1]
    l = torch.from_numpy(l)
    w, h, ch = l.shape
    l = l.reshape(-1, ch)
    l = normalizer(l)
    l = l.to('cuda')
    l = autoencoder.encode(l)
    l = l.reshape(w, h, 3)

    l = l.detach().cpu().numpy()

    l_norm = (l - l.min((0, 1))) / l.max((0, 1))

    plt.figure()
    plt.imshow(l_norm)
    plt.show()


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
    hparams['num_workers'] = 0

    hparams['bands'] = len(util.get_wavelengths_for(opt.camera_type))

    print("Hparams: %s" % hparams)

    all_records = get_for_camera_type(get_for_fruit(all_fruits, hparams['fruit']), hparams['camera_type'])

    # use only a part of the recordings
    selected_records = np.random.choice(all_records, 20)

    autoencoder = FalseColorAutoencoderModule(hparams, selected_records)
    logger = WandbLogger(hparams['git_id'], offline=not opt.online_logging,
                         save_dir=opt.log_path, project='deephs_pretrained_autoencoder')

    checkpoint_callback = ModelCheckpoint(
        filepath='best.ckpt',
        save_top_k=1,
        verbose=True,
        monitor='val_loss',
        mode='min'
    )

    trainer = lightning.Trainer(max_epochs=200, gpus=-1, logger=logger,
                                checkpoint_callback=checkpoint_callback)

    trainer.fit(autoencoder)
    best_autoencoder = FalseColorAutoencoderModule.load_from_checkpoint(checkpoint_callback.best_model_path,
                                                                        all_records=selected_records)

    plot_encoded_img(best_autoencoder.model,
                     np.random.choice(get_for_fruit(get_for_camera_type(all_fruits, CameraType.VIS),
                                                    Fruit.AVOCADO), 1)[0])

    # /// CLASSIFIER
    classifier = FalseColorClassifierModule(hparams, best_autoencoder.model)
    logger = WandbLogger(hparams['git_id'], offline=not opt.online_logging,
                         save_dir=opt.log_path, project='deephs_pretrained_classifier')

    early_stop_callback = EarlyStopping(
        monitor='val_loss',
        min_delta=0.00,
        patience=3,
        verbose=False,
        mode='max'
    )

    checkpoint_callback = ModelCheckpoint(
        filepath='best.ckpt',
        save_top_k=1,
        verbose=True,
        monitor='val_loss',
        mode='min'
    )

    trainer = lightning.Trainer(max_epochs=opt.num_epochs, gpus=-1, logger=logger, min_epochs=50,
                                early_stop_callback=early_stop_callback,
                                checkpoint_callback=checkpoint_callback)
    trainer.fit(classifier)

    for i in range(5):
        plot_encoded_img(classifier.model.autoencoder,
                         np.random.choice(get_for_fruit(get_for_camera_type(all_fruits, CameraType.VIS), Fruit.AVOCADO), 1)[0])



