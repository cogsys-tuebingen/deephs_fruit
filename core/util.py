import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import animation
from sklearn.cluster import KMeans
from PIL import Image
import gc
import torch

from core.name_convention import *
import core.spectral_io as spectral_io


def mask_background(_envi_data):
    _background_mask, _envi_data = get_background_mask(_envi_data)
    _background_mask = np.matmul(_background_mask, [[[True for i in range(_envi_data.shape[2])]]])
    _envi_data = np.ma.masked_array(_envi_data, mask=_background_mask)
    return _envi_data


def get_background_mask(_envi_data):
    # find the background
    avg_data = np.mean(_envi_data, 2, keepdims=True)
    _background_mask = avg_data < 0.2
    # replace some border effects
    _background_mask[:, :150, :] = True
    _background_mask[:, 1970:, :] = True
    return _background_mask, _envi_data


def get_n_spectra(_envi_data, _num, _only_obj):
    if not _only_obj:
        _used_data = _envi_data.reshape(_envi_data.shape[0] * _envi_data.shape[1], -1)
        _pixel_ids = np.random.randint(0, _used_data.shape[0], _num)
        _spectra = _used_data[_pixel_ids, :]
    else:
        _masked_envi = mask_background(_envi_data)
        _used_data = _masked_envi.reshape(_masked_envi.shape[0] * _masked_envi.shape[1], -1)
        _used_data = _used_data[np.logical_not(_used_data[:, 0].mask).squeeze()]

        _pixel_ids = np.random.randint(0, len(_used_data), _num)
        _spectra = _used_data[_pixel_ids, :]

    return _spectra


def display_hyper_spectral_data(_data, _band=None):

    fig = plt.figure()

    cmap = 'gray'

    if _band is None and _data.shape[2] > 3:
        ims = []

        for i in range(_data.shape[2]):
            ims.append([plt.imshow(_data[:, :, i].squeeze(), animated=True, cmap=cmap)])

        anim = animation.ArtistAnimation(fig, ims, interval=60, blit=True)

    elif _data.shape[2] == 3:
        plt.imshow(_data[:, :])
    elif _band is None:
        plt.imshow(_data[:, :, 0].squeeze(), cmap=cmap)
    else:
        plt.imshow(_data[:, :, _band].squeeze(), cmap=cmap)
    plt.show()


def display_all_bands(_data):


    fig, axes = plt.subplots(_data.shape[2], 1)

    for i in range(_data.shape[2]):
        axes[i].imshow(_data[:, :, i].squeeze())

    plt.show()


def plot_3d_data(_data, _colors=None):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    _d = _data.reshape((-1, 3))
    ax.scatter3D(_d[:,  0], _d[:, 1], _d[:, 2], c=_colors)
    fig.show()
    plt.show()


def kmeans(_data, _num_of_clusters):
    _kmeans = KMeans(_num_of_clusters)
    _kmeans.fit(_data)
    return _kmeans.predict(_data)


def write_array_image(_img, _name):
    """
        write a grayscale image into file
    :param _img:
    :param _name:
    :return:
    """

    # normalize the data
    if _img.ndim > 2:
        _normalized_img = _img.reshape(-1, _img.shape[2])
        # TODO: problems with negative values, they move the average around
        # _normalized_img = _normalized_img.clip(0, None)
        _normalized_img = (_normalized_img - _normalized_img.min(axis=0)) / (_normalized_img - _normalized_img.min(axis=0)).max(axis=0)
        _normalized_img = _normalized_img.reshape(_img.shape)
        _img = _normalized_img

    Image.fromarray((_img.squeeze() * 255).astype(np.uint8)).save(_name)
    print("# Wrote grayscale image to: %s" % _name)


def load_image_array(_name):
    """
        load a grayscale image from file

    :param _name:
    :param _base_path:
    :return:
    """
    img = Image.open(_name)
    print("# Load grayscale image from: %s" % _name)
    return img


def get_wavelengths_for(_c: CameraType):
    if _c == CameraType.VIS:
        return spectral_io.VIS_BANDS
    if _c == CameraType.NIR:
            return spectral_io.NIR_BANDS


def plot_spectra(_spectra, _bands, _legend=None, _areas=None):
    plt.figure()
    plt.xlabel("Wellenlänge")
    plt.ylabel("Intensität (Reflektanz)")

    if _spectra.ndim == 1:
        plt.plot(_bands, _spectra)
        if _areas is not None:
            plt.fill_between(_bands, _areas.min, _areas.max)
    else:
        for _c, _s in enumerate(_spectra):
            plt.plot(_bands, _s)
            if _areas is not None:
                plt.fill_between(_bands, _areas[_c]['min'], _areas[_c]['max'], alpha=0.2)

    if _legend is not None:
        plt.legend(_legend)

    plt.show()


def get_random_spectra(_data, _number):
    _internal_data = _data.reshape(-1, _data.shape[-1])
    _idx = np.random.randint(0, _internal_data.shape[0], _number)
    return _internal_data[_idx]


def split_into_train_and_test_fixed_and_evenly(_list, _ratio):
    """
    This method is randomness independent
    """
    if _ratio == 0:
        return _list, []

    if _ratio == 1:
        return [], _list

    record_count = len(_list)
    _labeled = np.array(_list)
    _validation_set_size = (record_count * _ratio)
    _each_nth_element = record_count / _validation_set_size

    _idx = []
    _i = 0.0
    while _i < record_count:
        _idx.append(int(_i))
        _i += _each_nth_element

    _mask = np.full(record_count, False, dtype=bool)
    _mask[_idx] = True
    _validation = _labeled[_mask]
    _train = np.array(_labeled[~_mask])

    return _train, _validation


def split_into_train_and_val(_list, _ratio):
    record_count = len(_list)
    _labeled = np.array(_list)
    _validation_set_size = int(record_count * _ratio)
    _idx = np.random.randint(record_count, size=_validation_set_size)
    _mask = np.full(record_count, False, dtype=bool)
    _mask[_idx] = True
    _validation = _labeled[_mask]
    _train = np.array(_labeled[~_mask])

    return _train, _validation


def mem_report():
    print("### BEGIN - Memory Report ###")
    for obj in gc.get_objects():
        if torch.is_tensor(obj):
            print("# \t %s : device %s with size %s" % (type(obj), obj.device, obj.size()))
    print("### END - Memory Report ###")


class MemoryCheckpoint:
    def __init__(self):
        self.mem_report_checkpoint_objs = []

    def checkpoint(self):
        print("### Checkpoint - Memory Report ###")
        mem_report_checkpoint_objs = []
        for obj in gc.get_objects():
            if torch.is_tensor(obj):
                self.mem_report_checkpoint_objs.append(obj)

    def print_since_checkpoint(self):
        print("### BEGIN - Memory Report since Checkpoint ###")
        for obj in gc.get_objects():
            if torch.is_tensor(obj) and obj not in self.mem_report_checkpoint_objs:
                print("# \t %s : device %s with size %s" % (type(obj), obj.device, obj.size()))
        print("### END - Memory Report ###")