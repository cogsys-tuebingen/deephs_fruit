import argparse

import pytorch_lightning as lightning
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.loggers.wandb import WandbLogger
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
import random

from classification.train import (
    AUGMENTATION_CONFIG_TRAIN,
    AUGMENTATION_CONFIG_TTA,
    CAMERA_AGNOSTIC_MODELS,
    DeepHsModule,
    get_args,
    get_parser,
)
from classification.transformers.linear_interpolation import LinearInterpolation
from classification.transformers.padding_in_channels import ChannelPadding

from classification.transformers.data_augmentation import Augmenter
from classification.transformers.normalize import Normalize
from core.datasets.hyperspectral_dataset import HyperspectralDataset, get_records
from core.lightning_callbacks.lr_logger import LRLoggingCallback
from core.name_convention import *
from core.run_utils import (
    get_current_git_hash,
    get_slurm_job_id,
    get_slurm_job_path,
    get_wandb_log_dir,
)
import core.util as util


def collate_fn_add_padding_for_channels(samples):
    """
        extend every sample to the same max_channels for torch.stack. Empty channels can be identified by -1 wavelength
    Args:
        samples:

    Returns:

    """
    channels_in_sample = [len(wavelengths)
                          for _, _, wavelengths in samples]
    max_channels = max(channels_in_sample)
    batch_size = len(samples)
    recording_shape = samples[0][0].shape[1:]

    for sample in samples:
        assert sample[0].shape[1:] == recording_shape

    xs = torch.zeros(batch_size, max_channels, *
                     recording_shape).type_as(samples[0][0])
    wavelengths = torch.ones(
        batch_size, max_channels).type_as(samples[0][1]) * -1

    for i, sample in enumerate(samples):
        xs[i, :len(sample[0])] = sample[0]
        wavelengths[i, :len(sample[2])] = sample[2]

    return xs, torch.stack([s[1] for s in samples]), wavelengths


class DeepHsModuleMultiCamera(DeepHsModule):
    def __init__(self, hparams):
        super(DeepHsModuleMultiCamera, self).__init__(hparams)

    def setup(self, stage: str):
        self.train_records, self.val_records, self.test_records = [], [], []

        for ct in self.hparams['camera_type']:
            train_records, val_records, test_records = \
                get_records(self.hparams['fruit'],
                            ct,
                            self.hparams['classification_type'],
                            use_inter_ripeness_levels=True,
                            extend_by_time_assumption=True,
                            use_new_recordings=True
                            )
            if ct == CameraType.VIS:
                self.train_records += train_records
                self.val_records += val_records
            elif not self.hparams['train_on_specim_only']:
                if self.hparams['second_camera_train_ratio'] < 0:
                    pass
                if self.hparams['second_camera_train_ratio'] < 1:
                    self.train_records += random.sample(train_records, int(
                        self.hparams['second_camera_train_ratio'] * len(train_records)))
                    self.val_records += random.sample(val_records,
                                                      int(self.hparams['second_camera_train_ratio'] * len(val_records)))
                else:
                    self.train_records += train_records
                    self.val_records += val_records
            self.test_records += test_records

        common_preprocessing = []
        common_preprocessing.append(Normalize(None))

        if self.hparams['interpolate_bands']:
            common_preprocessing.append(LinearInterpolation(self.hparams['bands'],
                                                            self.hparams['wavelength_range']))
        if self.hparams['use_padding_instead_interpolation']:
            common_preprocessing.append(ChannelPadding(self.hparams['bands']))

        if stage == 'fit':

            train_preprocessing = []
            train_preprocessing += [Augmenter(augmentation_config=self.hparams['augmentation_config'],
                                              input_size=self.hparams['input_size'])]
            self.train_dataset = HyperspectralDataset(self.hparams['classification_type'], self.train_records,
                                                      data_path=self.hparams['data_path'],
                                                      balance=True,
                                                      transform=transforms.Compose(
                                                          train_preprocessing + common_preprocessing),
                                                      input_size=self.hparams['input_size'])
            self.val_dataset = HyperspectralDataset(self.hparams['classification_type'],
                                                    self.val_records,
                                                    data_path=self.hparams['data_path'],
                                                    transform=transforms.Compose(
                                                        common_preprocessing),
                                                    input_size=self.hparams['input_size'])
        elif stage == 'test':
            self.test_dataset = HyperspectralDataset(self.hparams['classification_type'], self.test_records,
                                                     data_path=self.hparams['data_path'],
                                                     transform=transforms.Compose(
                                                         common_preprocessing),
                                                     input_size=self.hparams['input_size'])

    def train_dataloader(self) -> DataLoader:
        return DataLoader(self.train_dataset, self.hparams['batch_size'], num_workers=self.hparams['num_workers'],
                          shuffle=True, drop_last=True, collate_fn=collate_fn_add_padding_for_channels)


def get_additional_parameters():
    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    parser = get_parser()
    parser.add_argument("--linear_interpolation_bins", default=200, type=int,
                        help='The number of bins of the linear interpolation')
    parser.add_argument("--force_linear_interpolation", default=False, type=str2bool,
                        help='If you want to add linear interpolation for a camera agnostic model')
    parser.add_argument("--use_padding_instead_interpolation",
                        type=str2bool, default=False)
    parser.add_argument("--train_on_specim_only",
                        type=str2bool, default=False)
    parser.add_argument("--simulate_multiple_cameras",
                        type=str2bool, default=False)
    parser.add_argument("--second_camera_train_ratio", type=float, default=1.0)
    return parser


def main(hparams):
    hparams['type'] = 'multi_camera'
    hparams['git_id'] = get_current_git_hash()
    hparams['slurm_job_id'] = get_slurm_job_id()
    hparams['slurm_job_path'] = get_slurm_job_path()
    hparams['num_workers'] = 2

    hparams['camera_type'] = [CameraType.VIS, CameraType.VIS_COR]
    hparams['bands'] = max([len(util.get_wavelengths_for(c))
                            for c in hparams['camera_type']])
    hparams['wavelength_range'] = (350, 1100)
    if hparams['use_padding_instead_interpolation']:
        print(f"# Use padding to max bands {hparams['bands']}")
    hparams['interpolate_bands'] = (not hparams['use_padding_instead_interpolation']) and (
            hparams['force_linear_interpolation'] or hparams['model'] not in CAMERA_AGNOSTIC_MODELS)
    if hparams['interpolate_bands']:
        hparams['bands'] = hparams['linear_interpolation_bins']
        print(f"# Interpolate to {hparams['bands']} in range {hparams['wavelength_range']}")
    hparams['augmentation_config'] = AUGMENTATION_CONFIG_TRAIN
    hparams['tta_augmentation_config'] = AUGMENTATION_CONFIG_TTA
    hparams['tta_augmentation_iterations'] = 5
    hparams['num_classes'] = 3

    if 'input_size' not in hparams.keys():
        hparams['input_size'] = (64, 64)
    hparams['test_augmentation'] = True
    hparams['balance'] = True
    hparams['lr_scheduler'] = torch.optim.lr_scheduler.StepLR

    print("Hparams: %s" % hparams)

    model = DeepHsModuleMultiCamera(hparams)
    logger = WandbLogger(offline=not hparams['online_logging'], save_dir=hparams['log_path'],
                         project='deephs') if 'logger' not in hparams.keys() else hparams['logger']

    early_stop_callback = EarlyStopping(
        monitor='val/loss',
        min_delta=0.00,
        verbose=True,
        mode='min',
        patience=20
    )

    checkpoint_callback = ModelCheckpoint(
        filename='best',
        save_top_k=1,
        verbose=True,
        monitor='val/loss',
        mode='min'
    )

    trainer = lightning.Trainer(max_epochs=opt.num_epochs, gpus=0, logger=logger,
                                strategy='ddp',
                                min_epochs=50,
                                callbacks=[LRLoggingCallback(),
                                           early_stop_callback,
                                           checkpoint_callback
                                           ],
                                log_every_n_steps=1,
                                num_sanity_val_steps=0)

    trainer.fit(model)
    best_model = DeepHsModuleMultiCamera.load_from_checkpoint(
        checkpoint_callback.best_model_path)

    print(f"Best model [{checkpoint_callback.best_model_path}]..")
    result = trainer.test(best_model)
    return result[0]


if __name__ == "__main__":
    opt = get_args(get_additional_parameters)
    num_gpus = torch.cuda.device_count()

    # fix the seed for reproducibility
    seed = opt.seed
    lightning.utilities.seed.seed_everything(seed)

    if get_wandb_log_dir() is not None:
        opt.log_path = get_wandb_log_dir()

    hparams = vars(opt)

    main(hparams)
