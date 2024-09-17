
#get cpu num core py os
import os


import argparse

import pytorch_lightning as lightning
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.loggers import WandbLogger
import torch
from torch.utils.data import DataLoader
from torchvision import transforms 
import wandb

from classification.model_factory import get_model, VALID_MODELS, CAMERA_AGNOSTIC_MODELS
from classification.models.hyve.hyve_convolution import HyVEConv
from classification.transformers.data_augmentation import Augmenter
from classification.transformers.normalize import Normalize
from classification.utils.confusion_matrix import log_confusion_matrix
import core.argparser_utils as argparser_utils
from core.datasets.hyperspectral_dataset import HyperspectralDataset, get_records
from core.lightning_callbacks.lr_logger import LRLoggingCallback
from core.name_convention import CameraType, ClassificationType, Fruit
from core.run_utils import (
    get_current_git_hash,
    get_slurm_job_id,
    get_slurm_job_path,
    get_wandb_log_dir,
)
import core.util as util

import wandb
import torch






AUGMENTATION_CONFIG_TRAIN = {
    'random_flip': True,
    'random_rotate': True,
    'random_noise': False,
    'random_cut': True,
    'random_crop': True,
    'random_intensity_scale': False
}

AUGMENTATION_CONFIG_TTA = {
    'random_flip': True,
    'random_rotate': True,
    'random_noise': False,
    'random_cut': False,
    'random_crop': False,
    'random_intensity_scale': False
}


class DeepHsModule(lightning.LightningModule):
    def __init__(self, hparams):
        super(DeepHsModule, self).__init__()
        self.save_hyperparameters(hparams)
        self.model = get_model(self.hparams)
        self.critertion = torch.nn.CrossEntropyLoss()
        self.is_camera_agnostic = self.hparams['model'] in CAMERA_AGNOSTIC_MODELS
        self.train_records, self.val_records, self.test_records = None, None, None
        self.train_dataset, self.val_dataset, self.test_dataset = None, None, None

    def setup(self, stage: str):
        self.train_records, self.val_records, self.test_records = \
            get_records(self.hparams['fruit'],
                        self.hparams['camera_type'],
                        self.hparams['classification_type'],
                        use_inter_ripeness_levels=True,
                        extend_by_time_assumption=True,
                        allow_all_fruit_types=True
                        )

        common_preprocessing = [Normalize(self.hparams['camera_type'])]

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
                          shuffle=True, drop_last=True, collate_fn=None)

    def val_dataloader(self) -> DataLoader:
        return DataLoader(self.val_dataset, 1, num_workers=self.hparams['num_workers'],
                          shuffle=False)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, 1, num_workers=self.hparams['num_workers'])

    def forward(self, x, channel_wavelengths, test_augmentation=True):
        if test_augmentation:
            augmentation_config = self.hparams['tta_augmentation_config']
            augmenter = Augmenter(augmentation_config=augmentation_config,
                                  input_size=self.hparams['input_size'])

            iterations = self.hparams['tta_augmentation_iterations']

            preds = torch.zeros(
                (iterations, len(x), self.hparams['num_classes']))

            for i in range(iterations):
                # the augmentation should not change the label, so we can ignore it here.
                _batch = [augmenter((_x, _y, _channel_wavelengths)) for _x, _y, _channel_wavelengths in zip(
                    x.clone(), torch.zeros((x.shape[0], 1)), channel_wavelengths)]
                _x = torch.stack(list(zip(*_batch))[0])
                _channel_wavelengths = list(zip(*_batch))[2]
                if isinstance(_channel_wavelengths, torch.Tensor):
                    _channel_wavelengths = torch.stack(_channel_wavelengths)

                preds[i] = self.model(
                    _x, channel_wavelengths=list(_channel_wavelengths))

            pred = preds.mean(0)
        else:
            pred = self.model(x,
                              channel_wavelengths=channel_wavelengths)

        return pred

    @torch.no_grad()
    def predict(self, x, test_augmentation=True):
        return self.forward(x.cuda(), test_augmentation=test_augmentation).argmax(-1).detach().cpu()

    def training_step(self, batch, batch_id):
        x, y, channel_wavelengths = batch

        pred = self.model(x, channel_wavelengths=channel_wavelengths)
        loss = self.critertion(pred, y)
        assert torch.isnan(loss) == False
        accuracy = ((pred.argmax(1) == y).sum().float() / x.shape[0]).detach()
        self.log("train/loss", loss, on_step=True)
        self.log("train/accuracy", accuracy, on_step=True)

        if self.is_camera_agnostic:
            conv = self._get_hyve_conv()
            if conv is not None:
                for cw in channel_wavelengths:
                    _, activations = conv._get_gauss_features_and_activation(cw)
                for i, m in enumerate(activations):
                    self.log(
                        f"hyve_conv/gauss_activations_{i}", m, rank_zero_only=True)

        return loss

    def validation_step(self, batch, batch_id):
        x, y, channel_wavelengths = batch

        pred = self.model(x, channel_wavelengths=channel_wavelengths)
        loss = self.critertion(pred, y)

        accuracy = ((pred.argmax(1) == y).sum().float() / x.shape[0]).detach()

        self.log("val/loss", loss,
                 on_epoch=True, sync_dist=True)
        self.log("val/accuracy",
                 accuracy, on_epoch=True, sync_dist=True)

    def _get_hyve_conv(self) -> HyVEConv:
        conv = None
        if self.hparams['model'] in ('hyve'):
            conv = self.model.get_hyve_conv()

        return conv

    def validation_epoch_end(self, outputs):
        if self.is_camera_agnostic and self.trainer.is_global_zero:
            conv = self._get_hyve_conv()

            if conv is not None:
                gauss_mean, gauss_variance = conv.get_gauss().scaled_params()
                for i, m in enumerate(gauss_mean):
                    self.log(
                        f"hyve_conv/gauss_mean_{i}", m, rank_zero_only=True)
                for i, v in enumerate(gauss_variance):
                    self.log(
                        f"hyve_conv/gauss_variance_{i}", v, rank_zero_only=True)

                # log training progress of the hyve convolutions
                if self.current_epoch % 20 == 0:
                    if conv.share_features:
                        kernels_channelwise, kernels_gaussianwise, kernels_convwise = None, None, None
                        kernel_prototypes = conv._get_unweighted_kernels_shared()
                        if len(kernel_prototypes) == 3:
                            kernels_channelwise, kernels_gaussianwise, kernels_convwise = kernel_prototypes
                        else:
                            kernels_channelwise, kernels_convwise = kernel_prototypes

                        if kernels_channelwise is not None:
                            kernels_channelwise = kernels_channelwise.reshape(-1,
                                                                              kernels_channelwise.shape[-2],
                                                                              kernels_channelwise.shape[-1])
                            self.logger.experiment.log({f'hyve_conv/unweighted_kernels_channelwise':
                                                            [wandb.Image(kernel) for kernel in kernels_channelwise]})
                        if kernels_gaussianwise is not None:
                            kernels_gaussianwise = kernels_gaussianwise.reshape(-1,
                                                                                kernels_gaussianwise.shape[-2],
                                                                                kernels_gaussianwise.shape[-1])
                            self.logger.experiment.log({f'hyve_conv/unweighted_kernels_gaussianwise':
                                                            [wandb.Image(kernel) for kernel in kernels_gaussianwise]})
                        if kernels_convwise is not None:
                            kernels_convwise = kernels_convwise.reshape(-1,
                                                                        kernels_convwise.shape[-2],
                                                                        kernels_convwise.shape[-1])
                            self.logger.experiment.log({f'hyve_conv/unweighted_kernels_convwise':
                                                            [wandb.Image(kernel) for kernel in kernels_convwise]})

                        kernels = conv._get_unweighted_kernels_unmerged()
                        kernels = kernels.reshape(-1,
                                                  kernels.shape[-2], kernels.shape[-1])
                        self.logger.experiment.log({f'hyve_conv/unweighted_kernels_individual':
                                                        [wandb.Image(kernel) for kernel in kernels]})
                        for i, v in enumerate(conv.get_kernel_prototype_share_factors()):
                            if v is not None:
                                self.log(
                                    f"hyve_conv/kernel_share_impact_{i}", v, rank_zero_only=True)

                    kernels = conv.get_unweighted_kernels()
                    kernels = kernels.reshape(-1,
                                              kernels.shape[-2], kernels.shape[-1])
                    self.logger.experiment.log({f'hyve_conv/unweighted_kernels':
                                                    [wandb.Image(kernel) for kernel in kernels]})

    def test_step(self, batch, batch_id):
        x, y, channel_wavelengths = batch

        pred = self.forward(x,
                            channel_wavelengths=channel_wavelengths,
                            test_augmentation=self.hparams['test_augmentation'])
        pred = pred.to(y.device)
        loss = self.critertion(pred, y)
        accuracy = ((pred.argmax(1) == y).sum().float() / x.shape[0]).detach()

        return {
            'test_loss': loss,
            'test_accuracy': accuracy,
            'test_ys': torch.stack(
                [torch.tensor([y_pred, y_true]) for y_pred, y_true in zip(pred.argmax(1), y)])
        }

    def test_epoch_end(self, outputs):
        outputs = self.all_gather(outputs)
        test_accuracy = torch.stack([o['test_accuracy']
                                     for o in outputs]).mean()
        test_loss = torch.stack([o['test_loss']
                                 for o in outputs]).mean()
        test_ys = torch.cat([o['test_ys']
                             for o in outputs]).reshape(-1, 2).cpu().numpy()

        # log only in the first worker
        if self.trainer.is_global_zero:
            self.log('test/accuracy',
                     test_accuracy, rank_zero_only=True)
            self.log('test/loss',
                     test_loss, rank_zero_only=True)

            labels = []
            if self.hparams['classification_type'] == ClassificationType.RIPENESS:
                labels = ["Unripe", "Ripe", "Overripe"]
            elif self.hparams['classification_type'] == ClassificationType.FIRMNESS:
                labels = ["Too hard", "Perfect", "Too soft"]
            elif self.hparams['classification_type'] == ClassificationType.SUGAR:
                labels = ["Not sweet", "Perfect", "Too sweet"]

            log_confusion_matrix(
                self.logger, test_ys[:, 0], test_ys[:, 1], labels=labels)

    def configure_optimizers(self):
        self.optimizer = torch.optim.Adam(
            self.model.parameters(), lr=self.hparams['lr'])
        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, 30,
                                                         verbose=True)

        return {
            'optimizer': self.optimizer,
            'lr_scheduler': self.scheduler,
            'monitor': 'val_loss'
        }


def get_parser():
    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    parser = argparse.ArgumentParser(
        "DeepHS training:")
    parser.add_argument("--model", default="deephs_net", type=str,
                        choices=VALID_MODELS.keys())
    parser.add_argument("--batch_size", type=int, default=64,
                        help="The number of images per batch")
    parser.add_argument("--lr", type=float, default=1e-2)
    parser.add_argument(
        '--fruit', type=argparser_utils.str2fruit, default=Fruit.AVOCADO,
        choices=Fruit)
    parser.add_argument(
        '--camera_type', type=argparser_utils.str2cameratype, default=CameraType.VIS)
    parser.add_argument('--classification_type', type=argparser_utils.str2classification_type,
                        default=ClassificationType.FIRMNESS)
    parser.add_argument("--num_epochs", type=int, default=5000)
    parser.add_argument("--data_path", type=str, required=True,
                        help="the root folder of dataset")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--log_path", type=str, default=None)
    parser.add_argument("--online_logging", default=True, action='store_true') #online logging true
    parser.add_argument("--debug", default=False, action='store_true')
    parser.add_argument("--model_checkpoint", default=None, type=str)

    parser.add_argument("--comment", default=None, type=str)
    parser.add_argument("--camera_agnostic_num_gauss", default=5, type=int,
                        help='The number of gaussian distributions used for the camera agnostic convolution. Parameter G')

    return parser


def get_args(parser_generator=get_parser):
    args = parser_generator().parse_args()

    if args.fruit == Fruit.AVOCADO and args.classification_type == ClassificationType.SUGAR:
        print("! Avocados have no sugar label!")
        exit(0)

    args.hidden_layers = [25, 30, 50]

    return args


def main(hparams):
    hparams['type'] = 'single_camera'
    hparams['git_id'] = get_current_git_hash()
    hparams['slurm_job_id'] = get_slurm_job_id()
    hparams['slurm_job_path'] = get_slurm_job_path()
    hparams['num_workers'] = 4 if not hparams['debug'] else 0

    hparams['bands'] = len(util.get_wavelengths_for(hparams['camera_type']))
    hparams['wavelengths'] = util.get_wavelengths_for(hparams['camera_type'])
    hparams['augmentation_config'] = AUGMENTATION_CONFIG_TRAIN
    hparams['test_augmentation'] = True
    hparams['tta_augmentation_config'] = AUGMENTATION_CONFIG_TTA
    hparams['tta_augmentation_iterations'] = 5
    hparams['num_classes'] = 3
    hparams['input_size'] = (64, 64)

    print("Hparams: %s" % hparams)

    model = DeepHsModule(hparams)
    logger = WandbLogger(
    offline=not hparams.get('online_logging', True),  # Use parentheses here
    save_dir=hparams.get('log_path', './logs'),
    project='deephs') if 'logger' not in hparams else hparams['logger']

    

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



    

    num_cpu_cores = os.cpu_count() #ใช้ cpu 
    trainer = lightning.Trainer(max_epochs=opt.num_epochs,
                                accelerator='cpu',
                                devices=1,
                                logger=logger,
                                strategy=None,
                                min_epochs=2,
                                callbacks=[LRLoggingCallback(),
                                           early_stop_callback,
                                           checkpoint_callback
                                           ],
                                log_every_n_steps=1,
                                num_sanity_val_steps=0)

    trainer.fit(model)
    best_model = DeepHsModule.load_from_checkpoint(
        checkpoint_callback.best_model_path)
    best_model.eval()

    print(f"Best model [{checkpoint_callback.best_model_path}]..")
    result = trainer.test(best_model)

    return result[0]


if __name__ == "__main__":
    opt = get_args()
    #ปิด gpu
    #num_gpus = torch.cuda.device_count()

    # fix the seed for reproducibility
    seed = opt.seed
    lightning.utilities.seed.seed_everything(seed)

    if get_wandb_log_dir() is not None:
        opt.log_path = get_wandb_log_dir()

    hparams = vars(opt)

    main(hparams)
