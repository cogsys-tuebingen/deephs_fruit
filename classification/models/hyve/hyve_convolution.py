import collections.abc
from itertools import repeat

import torch
import torch.nn as nn
import torch.nn.functional as F
from .gaussian import GaussDistributionModule


def _ntuple(n):
    def parse(x):
        if isinstance(x, collections.abc.Iterable):
            return x
        return tuple(repeat(x, n))

    return parse


_pair = _ntuple(2)


class HyVEConv(nn.Module):
    def __init__(self, num_of_wrois, wavelength_range,
                 out_channels, kernel_size, stride=1, padding=0,
                 dilation=1, groups=1, bias=True, padding_mode='zeros', enable_extension=True,
                 stop_gaussian_gradient=False
                 ):
        """
            This is the official implementation of HyVEConv and HyVEConv++, which were proposed in
            "Wavelength-aware 2D Convolutions for Hyperspectral Imaging"

        Args:
            num_of_wrois: This is parameter G, which defines the number of used camera filters
            wavelength_range: A tuple, with: (min_wavelength, max_wavelength), necessary for the definition of the wavelength range.
            enable_extension: Enables HvVEConv++ (default: True)
            stop_gaussian_gradient: Prevent training of the Gaussians. Only for test purpose (default: False)
            out_channels: -> check torch.nn.Conv2d
            kernel_size: -> check torch.nn.Conv2d
            stride:  -> check torch.nn.Conv2d
            padding: -> check torch.nn.Conv2d
            dilation: -> check torch.nn.Conv2d
            groups: -> check torch.nn.Conv2d
            bias: -> check torch.nn.Conv2d
            padding_mode: -> check torch.nn.Conv2d


            @author --
        """
        super().__init__()

        self.out_channels = out_channels
        self.kernel_size = _pair(kernel_size)
        self.stride = _pair(stride)
        self.padding = _pair(padding)
        self.dilation = _pair(dilation)
        self.groups = groups
        self.padding_mode = padding_mode
        self.bias = bias
        self.wavelength_range = wavelength_range
        self.share_features = enable_extension
        assert isinstance(self.wavelength_range, list) or isinstance(
            self.wavelength_range, tuple)
        self.gauss_num = num_of_wrois
        self.gauss_variance_factor = (self.wavelength_range[1] - self.wavelength_range[0])

        self.gauss = GaussDistributionModule(self.gauss_num,
                                             self.wavelength_range[0],
                                             (self.wavelength_range[1] -
                                              self.wavelength_range[0]),
                                             self.gauss_variance_factor,
                                             equally_distributed=True)

        self.has_gradient_kernel_cell = True
        self.has_gradient_gauss = not stop_gaussian_gradient

        self.kernel_weights_individual = nn.parameter.Parameter(torch.ones((
            self.gauss_num,
            self.out_channels,
            self.kernel_size[0],
            self.kernel_size[1])))

        if self.share_features:
            self.kernel_weights_channelwise = nn.parameter.Parameter(torch.randn((
                1,
                self.out_channels,
                self.kernel_size[0],
                self.kernel_size[1])))
            self.kernel_weights_channelwise_factor = nn.parameter.Parameter(torch.tensor(0.1))
            self.kernel_weights_convwise = nn.parameter.Parameter(torch.ones((
                1,
                1,
                self.kernel_size[0],
                self.kernel_size[1])))
            self.kernel_weights_convwise_factor = nn.parameter.Parameter(torch.tensor(0.1))

        if self.bias:
            self.bias_tensor = nn.parameter.Parameter(torch.zeros(
                [self.out_channels]))

        self.initialize()

    def initialize(self):
        self.gauss.initialize_weights()

        # init kernel weights
        nn.init.kaiming_normal_(self.kernel_weights_individual, mode='fan_in')
        if self.share_features:
            nn.init.kaiming_normal_(
                self.kernel_weights_convwise, mode='fan_in')
            if self.kernel_weights_channelwise is not None:
                nn.init.kaiming_normal_(
                    self.kernel_weights_channelwise, mode='fan_in')
        if self.bias:
            nn.init.constant_(self.bias_tensor, 0)

    def get_gauss(self) -> GaussDistributionModule:
        return self.gauss

    def get_unweighted_kernels(self):
        if self.share_features:
            kernel = self.kernel_weights_individual

            if self.kernel_weights_convwise is not None:
                kernel = kernel + self.kernel_weights_convwise_factor * self.kernel_weights_convwise.repeat(
                    self.gauss_num, self.out_channels, 1, 1)
            if self.kernel_weights_channelwise is not None:
                kernel = kernel + self.kernel_weights_channelwise_factor * self.kernel_weights_channelwise.repeat(
                    self.gauss_num, 1, 1, 1)
            return kernel
        else:
            return self.kernel_weights_individual

    def _get_unweighted_kernels_unmerged(self):
        return self.kernel_weights_individual

    def _get_unweighted_kernels_shared(self):
        return (self.kernel_weights_channelwise,
                self.kernel_weights_convwise)

    def get_kernel_prototype_share_factors(self):
        return (self.kernel_weights_channelwise_factor,
                self.kernel_weights_convwise_factor)

    def _get_gauss_features_and_activation(self, channel_wavelengths):
        gauss_features = self.gauss(channel_wavelengths)

        return gauss_features, gauss_features.sum(0)

    def predict_kernel(self, channel_wavelengths):
        gauss_features, _sums = self._get_gauss_features_and_activation(
            channel_wavelengths)

        kernel_weights = self.get_unweighted_kernels()

        if not self.has_gradient_gauss:
            gauss_features = gauss_features.detach()

        if not self.has_gradient_kernel_cell:
            kernel_weights = kernel_weights.detach()

        weight = torch.matmul(
            gauss_features, kernel_weights.view(self.gauss_num, -1))

        weight = weight.view(len(channel_wavelengths), self.out_channels,
                             self.kernel_size[0], self.kernel_size[1])
        return weight.permute(1, 0, 2, 3)

    def _remove_padding_channels(self, channel_wavelengths, x):
        return channel_wavelengths[channel_wavelengths > 0], x[channel_wavelengths > 0]

    def _prepare_channel_wavelengths(self, channel_wavelengths):
        if isinstance(channel_wavelengths, list) and isinstance(channel_wavelengths[0], float):
            channel_wavelengths = torch.tensor(channel_wavelengths).float()

        if isinstance(channel_wavelengths, list):
            channel_wavelengths = torch.stack(channel_wavelengths)

        return channel_wavelengths

    def _multiple_channel_definitions(self, channel_wavelengths):
        return channel_wavelengths.dim() > 1 and not (channel_wavelengths == channel_wavelengths[0]).all()

    def _apply_conv2d(self, x, weight):
        if not self.bias:
            out = F.conv2d(x, weight=weight, stride=self.stride, padding=self.padding, dilation=self.dilation,
                           groups=self.groups)
        else:
            out = F.conv2d(x, weight=weight, bias=self.bias_tensor, stride=self.stride, padding=self.padding,
                           dilation=self.dilation, groups=self.groups)

        return out

    def forward(self, x, channel_wavelengths):
        channel_wavelengths = self._prepare_channel_wavelengths(channel_wavelengths)
        if self._multiple_channel_definitions(channel_wavelengths):
            # the inputs cover different channel
            result = []
            weights = {}
            for _channel_wavelengths, _x in zip(channel_wavelengths, x):
                _channel_wavelengths, _x = self._remove_padding_channels(
                    _channel_wavelengths, _x)

                key = tuple(_channel_wavelengths.tolist())
                if key not in weights.keys():
                    weights[key] = self.predict_kernel(_channel_wavelengths)
                weight = weights[key]

                out_features = self._apply_conv2d(_x.unsqueeze(0), weight)

                result.append(out_features)

            result = torch.cat(result)
            return result.type_as(x)

        else:
            weight = self.predict_kernel(channel_wavelengths[0] if channel_wavelengths.dim() > 1 else channel_wavelengths)
            res = self._apply_conv2d(x, weight)
            return res






