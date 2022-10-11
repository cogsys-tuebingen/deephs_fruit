from core.name_convention import *
import numpy as np
import torch


def nearest_idx(x, options, number):
    return torch.argsort(torch.abs(x - options))[:number]


class LinearInterpolation(object):
    def __init__(self, n_output_channels, wavelength_range, interpolate=True):
        self.n_channels = n_output_channels
        self.wavelength_range = wavelength_range

        assert len(wavelength_range) == 2
        min_wavelength = min(wavelength_range)
        max_wavelength = max(wavelength_range)
        step_size = (max_wavelength - min_wavelength) / n_output_channels
        self.output_channel_wavelengths = torch.tensor([min_wavelength + i *
                                                        step_size for i in
                                                        range(self.n_channels)])

        self.cached_weights = {}
        self.interpolate = interpolate

    def __call__(self, sample):
        x, y, in_channel_wavelengths = sample
        key = str(in_channel_wavelengths)

        if key not in self.cached_weights.keys():
            min_in_wavelength_idx = np.argmin(in_channel_wavelengths)
            max_in_wavelength_idx = np.argmax(in_channel_wavelengths)

            self.cached_weights[key] = []

            if self.interpolate:
                for i, output_channel_wavelength in enumerate(self.output_channel_wavelengths):
                    if output_channel_wavelength <= in_channel_wavelengths[min_in_wavelength_idx]:
                        self.cached_weights[key].append(
                            [min_in_wavelength_idx])
                    elif output_channel_wavelength >= in_channel_wavelengths[max_in_wavelength_idx]:
                        self.cached_weights[key].append(
                            [max_in_wavelength_idx])
                    else:
                        nearest_a_idx, nearest_b_idx = nearest_idx(
                            output_channel_wavelength, in_channel_wavelengths, 2)
                        diff_a = np.abs(
                            in_channel_wavelengths[nearest_a_idx] - output_channel_wavelength)
                        diff_b = np.abs(
                            in_channel_wavelengths[nearest_b_idx] - output_channel_wavelength)
                        weight_a = 1 - (diff_a / (diff_a + diff_b))
                        weight_b = 1 - weight_a
                        self.cached_weights[key].append(
                            [weight_a, nearest_a_idx, weight_b, nearest_b_idx])
            else:
                for i, output_channel_wavelength in enumerate(self.output_channel_wavelengths):
                    idx = nearest_idx(output_channel_wavelength,
                                      in_channel_wavelengths, 1)
                    self.cached_weights[key].append([1.0, idx])

        weights = self.cached_weights[key]

        x_out = torch.zeros(self.n_channels, x.shape[1], x.shape[2]).type_as(x)
        for i, (output_channel_wavelength, weight) in enumerate(zip(self.output_channel_wavelengths, weights)):
            if len(weight) == 1:
                x_out[i, :, :] = x[weight, :, :]
            elif len(weight) == 2:
                _, idx =  weight

                x_out[i, :, :] = x[idx, :, :]
            else:
                weight_a, idx_a, weight_b, idx_b = weight

                x_out[i, :, :] = weight_a * \
                    x[idx_a, :, :] + weight_b * x[idx_b, :, :]

        return (x_out, y, self.output_channel_wavelengths)


if __name__ == '__main__':
    from core.fruit_list import *
    import time
    import spectral
    import spectral.io.envi as envi
    import core.util as util

    def load_envi(path):
        _exts = '.bin'
        if not os.path.exists('%s%s' % (path, _exts)):
            _exts = '.img'

        if not os.path.exists('%s%s' % (path, _exts)):
            raise spectral.io.spyfile.FileNotFoundError(
                "Could not find data for: %s" % path)

        envi_header = envi.open('%s.hdr' % path, image='%s%s' % (path, _exts))
        envi_data = envi_header.load()
        return envi_header, envi_data

    def load_cube(path):
        _raw_envi_header, _raw_envi_data = load_envi(path)
        _white_envi_header, _white_envi_data = load_envi(path + "_White")
        _dark_envi_header, _dark_envi_data = load_envi(path + "_Dark")

        return spectral_io.use_references(_raw_envi_data, _white_envi_data, _dark_envi_data)

    data = load_cube(
        "/data/measurements/Messung/Kiwi/VIS/day_01/kiwi_day_01_22_front")
    data = torch.from_numpy(np.array(data).transpose(2, 0, 1))

    func = LinearInterpolation(244, (350, 1200), interpolate=False)

    start = time.time()
    result, _, wavelengths = func(
        [data, None, np.array(util.get_wavelengths_for(CameraType.VIS))])
    result, _, wavelengths = func(
        [data, None, np.array(util.get_wavelengths_for(CameraType.VIS))])
    result, _, wavelengths = func(
        [data, None, np.array(util.get_wavelengths_for(CameraType.VIS))])
    result, _, wavelengths = func(
        [data, None, np.array(util.get_wavelengths_for(CameraType.VIS))])
    print("Took %f" % (time.time() - start))

    import matplotlib.pyplot as plt

    c = (100, 101, 100)

    plt.figure()
    plt.imshow(result.permute(1, 2, 0)[:, :, c])
    plt.show()
