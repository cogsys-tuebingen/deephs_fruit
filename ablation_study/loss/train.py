import pytorch_lightning as lightning
from pytorch_lightning.loggers.wandb import WandbLogger
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.callbacks import ModelCheckpoint
import torch

import argparse
import random

from core.run_utils import get_current_git_hash
from core.name_convention import *
import core.argparser_utils as argparser_utils
from core.loss.focalloss import FocalLoss
from classification.train import DeepHsModule
from classification.transformers.data_augmentation import AUGMENTATION_CONFIG
from core.lightning_callbacks.lr_logger import LRLoggingCallback


ABLATION_TYPE = 'loss'


class DeepHsAblationStudyModule(DeepHsModule):
    def __init__(self, hparams):
        super(DeepHsAblationStudyModule, self).__init__(hparams)

        if hparams['loss'] == 'focal':
            self.critertion = FocalLoss(size_average=False)
        if hparams['loss'] == 'cross':
            self.critertion = torch.nn.CrossEntropyLoss()


def get_args():
    parser = argparse.ArgumentParser(
        f"DeepHS ablation_study {ABLATION_TYPE}:")
    parser.add_argument("--batch_size", type=int, default=32, help="The number of images per batch")
    parser.add_argument("--lr", type=float, default=1e-2)
    parser.add_argument('--fruit', type=argparser_utils.str2fruit, default=Fruit.AVOCADO)
    parser.add_argument('--camera_type', type=argparser_utils.str2cameratype, default=CameraType.VIS)
    parser.add_argument('--classification_type', type=argparser_utils.str2classification_type,
                        default=ClassificationType.FIRMNESS)
    parser.add_argument("--num_epochs", type=int, default=5000)
    parser.add_argument("--data_path", type=str, default="", help="the root folder of dataset")
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

    parser.add_argument("--loss", default="focal_loss", type=str)

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
    hparams['ablation'] = ABLATION_TYPE
    hparams['git_id'] = get_current_git_hash()
    hparams['batch_size'] = opt.batch_size
    hparams['num_workers'] = 8

    hparams['bands'] = len(util.get_wavelengths_for(opt.camera_type))
    hparams['augmentation_config'] = AUGMENTATION_CONFIG
    hparams['test_augmentation'] = True

    print("Hparams: %s" % hparams)

    model = DeepHsAblationStudyModule(hparams)
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
    best_model = DeepHsAblationStudyModule.load_from_checkpoint(checkpoint_callback.best_model_path)

    print("Best model..")
    trainer.test(best_model)
