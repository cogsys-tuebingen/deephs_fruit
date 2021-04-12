"""
 logs the current learing rate each epoch
"""

import pytorch_lightning


class LRLoggingCallback(pytorch_lightning.Callback):
    def on_train_epoch_start(self, trainer: pytorch_lightning.Trainer, pl_module):
        current_lr = trainer.optimizers[0].param_groups[0]['lr']
        trainer.logger.experiment.log({"current_lr": current_lr})
