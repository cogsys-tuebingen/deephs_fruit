import torch.nn.functional as F

from core.name_convention import *


class ChannelPadding(object):
    def __init__(self, n_output_channels):
        self.n_channels = n_output_channels

    def __call__(self, sample):
        x, y, in_channel_wavelengths = sample

        assert len(x) <= self.n_channels

        if len(x) == self.n_channels:
            return sample

        missing_channels = self.n_channels - len(x)
        x_out = F.pad(x, (0, 0, 0, 0, 0, missing_channels), 'constant', 0)
        out_channel_wavelengths = F.pad(
            in_channel_wavelengths, (0, missing_channels), 'constant', -1)

        return (x_out, y, out_channel_wavelengths)


if __name__ == '__main__':
    import torch
    x = torch.ones((224, 64, 64))
    func = ChannelPadding(264)

    o, _, _ = func((x, None, torch.tensor(list(range(224)))))

    print(o.shape)
