import pytorch_lightning as lightning
from pytorch_lightning.loggers.wandb import WandbLogger
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.callbacks import ModelCheckpoint
import torch

import tqdm
import argparse
import random
from torch.utils.data import DataLoader

from core.run_utils import get_current_git_hash
from core.fruit_list import *
import core.argparser_utils as argparser_utils
from core.loss.focalloss import FocalLoss

from extract_fruit.layer_classifier import LayerClassifierModel
from extract_fruit.extractor import extract_obj_by_mask, store_object, exists, extract


def extract_pixels(path, fruit: FruitRecord):
    mask_path = os.path.join(path, fruit.fruit.value, fruit.camera_type.value, "masks",
                             "%s.mask.png" % get_name(fruit.fruit, fruit.id, fruit.side, fruit.day))
    if not os.path.exists(mask_path):
        return None

    _envi_header, _envi_data = fruit.load(path)

    img = util.load_image_array(mask_path)
    layer_mask = np.array(img)[:, :, 0:1]

    # get the indices for the different layer types
    layer_mask_list = layer_mask.reshape(-1, 1)
    background_pixel_idx = np.where(layer_mask_list == 0)[0]
    forground_pixel_idx = np.where(layer_mask_list == 255)[0]

    ambiguous_pixel_idx = np.where(np.logical_and(layer_mask_list < 255, layer_mask_list > 0))[0]

    # now retrieve the pixels for each layer
    _envi_data_list = _envi_data.reshape(-1, _envi_data.shape[2])
    _background_pixel = _envi_data_list[background_pixel_idx]
    _foreground_pixel = _envi_data_list[forground_pixel_idx]
    _ambiguous_pixel = _envi_data_list[ambiguous_pixel_idx]

    return _background_pixel, _foreground_pixel, _ambiguous_pixel


def get_records(all_records, path, camera_type):
    background_pixel = np.zeros((0, len(util.get_wavelengths_for(camera_type))))
    foreground_pixel = np.zeros((0, len(util.get_wavelengths_for(camera_type))))
    ambiguous_pixel = np.zeros((0, len(util.get_wavelengths_for(camera_type))))

    for record in tqdm.tqdm(all_records, "Extract pixels of masked records"):
        pixels = extract_pixels(path, record)

        if pixels is not None:
            background_pixel = np.append(background_pixel, pixels[0], axis=0)
            foreground_pixel = np.append(foreground_pixel, pixels[1], axis=0)
            ambiguous_pixel = np.append(ambiguous_pixel, pixels[2], axis=0)

    print("# Load background pixels %i" % len(background_pixel))
    print("# Load foreground pixels %i" % len(foreground_pixel))
    print("# Load ambiguous pixels %i" % len(ambiguous_pixel))

    labeled_pixels = []
    labeled_pixels += [(p, 0) for p in background_pixel]
    labeled_pixels += [(p, 1) for p in foreground_pixel]
    labeled_pixels = np.array(labeled_pixels)

    pixel_count = len(labeled_pixels)
    train_set_size = int(float(pixel_count) * 3 / 4)
    idx_train = np.random.choice(list(range(pixel_count)), train_set_size, replace=False)
    train_set_mask = np.zeros(pixel_count, dtype=bool)
    train_set_mask[idx_train] = True
    train_set = labeled_pixels[train_set_mask]
    val_set = labeled_pixels[np.logical_not(train_set_mask)]

    print("# Train set size %i" % len(train_set))
    print("# Val set size %i" % len(val_set))

    return train_set.tolist(), val_set.tolist()


class LayerClassifierModule(lightning.LightningModule):
    def __init__(self, hparams, all_records):
        super(LayerClassifierModule, self).__init__()
        self._estimator_type = 'classifier'

        self.hparams = hparams
        self.all_records = all_records

        self.model = LayerClassifierModel(hparams['bands'])
        self.critertion = FocalLoss()

    def setup(self, stage: str):
        self.train_dataset, self.val_dataset = get_records(self.all_records, self.hparams['data_path'],
                                                           self.hparams['camera_type'])

    def train_dataloader(self) -> DataLoader:
        return DataLoader(self.train_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'],
                          shuffle=True, drop_last=True)

    def val_dataloader(self) -> DataLoader:
        return DataLoader(self.val_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'],
                          shuffle=False)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'])

    def forward(self, x):
        return self.model(x)

    def predict(self, x):
        return self.forward(x).argmax(-1).detach()

    def training_step(self, batch, batch_id):
        x, y = batch

        pred = self.model(x.float())
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

        pred = self.model(x.float())
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
                'val_accuracy': val_accuracy
            }
        }

    def test_step(self, batch, batch_id):
        x, y = batch

        pred = self.model(x)
        loss = self.critertion(pred, y)
        accuracy = ((pred.argmax(1) == y).sum().float() / x.shape[0]).detach()

        return {
            'test_loss': loss,
            'test_accuracy': accuracy
        }

    def test_epoch_end(self, outputs):
        test_accuracy = torch.stack([o['test_accuracy'] for o in outputs]).mean()
        test_loss = torch.stack([o['test_loss'] for o in outputs]).mean()

        self.logger.experiment.summary['test_accuracy'] = test_accuracy
        self.logger.experiment.summary['test_loss'] = test_loss

        return {
            'log':
                {
                    'test_loss': test_loss,
                    'test_accuracy': test_accuracy,
                }
        }

    def configure_optimizers(self):
        self.optimizer = torch.optim.Adam(self.model.parameters(),
                                          lr=self.hparams['lr'])
        #self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, verbose=True, patience=2)
        #torch.optim.lr_scheduler.ExponentialLR(self.optimizer, 0.99)
        return [self.optimizer]# , [self.scheduler]


def get_args():
    parser = argparse.ArgumentParser(
        "DeepHS - LayerExtractor:")
    parser.add_argument("--batch_size", type=int, default=10000, help="The number of images per batch")
    parser.add_argument("--lr", type=float, default=1e-5)
    parser.add_argument('--fruit', type=argparser_utils.str2fruit, default=Fruit.AVOCADO)
    parser.add_argument('--camera_type', type=argparser_utils.str2cameratype, default=CameraType.VIS)
    parser.add_argument("--num_epochs", type=int, default=int(1e5))
    parser.add_argument("--data_path", type=str, default="", help="the root folder of dataset")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--log_path", type=str, default=None)
    parser.add_argument("--online_logging", default=False, action='store_true')
    parser.add_argument("--extract_fruit", default=False, action='store_true')
    parser.add_argument("--output_path", default=None, type=str)

    args = parser.parse_args()
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
    hparams['num_workers'] = 0

    hparams['bands'] = len(util.get_wavelengths_for(opt.camera_type))
    print("Hparams: %s" % hparams)

    all_records = get_for_camera_type(get_for_fruit(all_fruits, hparams['fruit']), hparams['camera_type'])

    model = LayerClassifierModule(hparams, all_records)
    logger = WandbLogger(hparams['git_id'], offline=not opt.online_logging,
                         save_dir=opt.log_path, project='deephs-layerclassifier')

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

    trainer = lightning.Trainer(max_epochs=opt.num_epochs, gpus=-1, logger=logger,
                                early_stop_callback=early_stop_callback, min_epochs=100,
                                checkpoint_callback=checkpoint_callback)

    trainer.fit(model)
    best_model = LayerClassifierModule.load_from_checkpoint(all_records=all_records,
                                                            checkpoint_path=checkpoint_callback.best_model_path)

    if hparams['extract_fruit']:
        if hparams['output_path'] is None:
            raise Exception("output_path is missing")

        extract(hparams['data_path'], hparams['output_path'], all_records, hparams['camera_type'], best_model)
