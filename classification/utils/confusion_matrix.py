from sklearn.metrics import plot_confusion_matrix, confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt


def create_confusion_matrix(y_pred, y_true, labels, normalize=True):
    np.set_printoptions(precision=2)

    cm = confusion_matrix(y_true, y_pred, sample_weight=None,
                          labels=None, normalize='true' if normalize else None)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=labels)

    disp.plot(include_values=True,
              cmap=plt.cm.Blues, ax=None, xticks_rotation='horizontal',
              values_format=None)

    disp.ax_.set_title("Normalized confusion matrix" if normalize else "Confusion matrix")
    return disp


def log_confusion_matrix(logger, y_pred, y_true, labels, normalize=True):
    disp = create_confusion_matrix(y_pred, y_true, labels, normalize)
    logger.experiment.log({'confusion_matrix': disp.figure_})