from core.name_convention import *
from core.util import get_wavelengths_for
import numpy as np
import torch
from classification.transformers.cie_table import CIE_CMF, D50

# XYZ to sRGB
# reference http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
XYZ_TO_sRGB = np.array([[3.2404542, - 1.5371385, - 0.4985314],
                        [-0.9692660, 1.8760108, 0.0415560],
                        [0.0556434, - 0.2040259, 1.0572252]])


class ToRGB(object):
    def __init__(self, camera_type: CameraType):
        self.camera_type = camera_type
        self.wavelengths = get_wavelengths_for(self.camera_type)

        self.cie_band_mapping = []
        for s_wavelength in CIE_CMF[:, 0]:
            band_idx = (np.abs(s_wavelength - self.wavelengths)).argmin()
            d50_idx = (np.abs(s_wavelength - D50[:, 0])).argmin()

            self.cie_band_mapping.append((band_idx, d50_idx))

        self.cie_band_mapping = np.array(self.cie_band_mapping)

    def _spectral_pixels_to_xyz(self, pixels):
        xyz_pixels = []

        Xs = np.matmul(pixels[:, self.cie_band_mapping[:, 0]], D50[self.cie_band_mapping[:, 1], 1] * CIE_CMF[:, 1])
        Ys = np.matmul(pixels[:, self.cie_band_mapping[:, 0]], D50[self.cie_band_mapping[:, 1], 1] * CIE_CMF[:, 2])
        Zs = np.matmul(pixels[:, self.cie_band_mapping[:, 0]], D50[self.cie_band_mapping[:, 1], 1] * CIE_CMF[:, 3])
        XYZs = Xs + Ys + Zs
        N = np.sum(D50[self.cie_band_mapping[:, 1], 1] * CIE_CMF[:, 3])

        Xs /= N
        Ys /= N
        Zs /= N

        return np.array([Xs, Ys, Zs])

    def _xyz_to_rgb(self, pixels):
        return np.matmul(XYZ_TO_sRGB, pixels)

    def _gamma_compression(self, pixels):
        # reference: https://mina86.com/2019/srgb-xyz-conversion/
        def to_non_linear(v):
            non_linear = 3294.6 * v if v <= 0.00313066844250060782371 else (269.025 * np.power(v, 5.0 / 12.0) - 14.025)
            return int(min(max(np.floor(non_linear), 0), 255))

        return np.vectorize(to_non_linear)(pixels)

    def __call__(self, sample):
        item, label = sample
        h, w = item.shape[1:]

        pixels = item.reshape(-1, h * w).numpy().transpose(1, 0)
        pixels_xyz = self._spectral_pixels_to_xyz(pixels)
        pixels_rgb = self._xyz_to_rgb(pixels_xyz)
        pixels_rgb = self._gamma_compression(pixels_rgb).astype(np.uint8)

        new_item = pixels_rgb.reshape((3, h, w))

        return torch.from_numpy(new_item), label


def normalize_img(img):
    """
        Use the ImageNet mean and std
    """

    img = img.astype(np.float) / 255.

    mean = np.array([[[0.485, 0.456, 0.406]]])
    std = np.array([[[0.229, 0.224, 0.225]]])

    img = ((img.astype(np.float).transpose(1, 2, 0) - mean) / std).transpose(2, 0, 1)

    return img


class NormalizeRGB(object):
    def __call__(self, sample):
        x, y = sample
        x = torch.from_numpy(normalize_img(x.numpy())).float()

        return (x, y)


if __name__ == '__main__':
    from core.hyperspectral_dataset import HyperspectralDataset
    from core.fruit_list import *
    import time
    import spectral
    import spectral.io.envi as envi

    def load_envi(path):
        _exts = '.bin'
        if not os.path.exists('%s%s' % (path, _exts)):
            _exts = '.img'

        if not os.path.exists('%s%s' % (path, _exts)):
            raise spectral.io.spyfile.FileNotFoundError("Could not find data for: %s" % path)

        envi_header = envi.open('%s.hdr' % path, image='%s%s' % (path, _exts))
        envi_data = envi_header.load()
        return envi_header, envi_data


    def load_cube(path):
        _raw_envi_header, _raw_envi_data = load_envi(path)
        _white_envi_header, _white_envi_data = load_envi(path + "_White")
        _dark_envi_header, _dark_envi_data = load_envi(path + "_Dark")

        return spectral_io.use_references(_raw_envi_data, _white_envi_data, _dark_envi_data)


    data = load_cube("/data/measurements/TestMeasurement/apfel1_front")
    # data = load_cube("/data/measurements/Messung/Kiwi/VIS/day_01/kiwi_day_01_22_front")
    data = torch.from_numpy(np.array(data).transpose(2, 0, 1))

    func = ToRGB(CameraType.VIS)

    start = time.time()
    result, _ = func([data, None])
    print("Took %f" % (time.time() - start))

    import matplotlib.pyplot as plt

    c = 100

    plt.figure()
    plt.imshow(result.permute(1, 2, 0))
    plt.show()
