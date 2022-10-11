import torch.nn as nn

from .hyve.hyve_convolution import HyVEConv


class DeepHSNet_with_HyVEConv(nn.Module):
    def __init__(self, bands, wavelength_range, num_of_wrois, enable_extension=True,
                 num_classes=3, stop_gaussian_gradient=False):
        super(DeepHSNet_with_HyVEConv, self).__init__()
        self.bands = bands
        self.hidden_layers = [25, 30, 50]

        self.wavelength_range = wavelength_range
        self.gauss_variance_factor = (wavelength_range[1] - wavelength_range[0])
        print(f"# Create classifier network for the bands between "
              f"{self.wavelength_range[0]} nm "
              f"and {self.wavelength_range[1]} nm")

        # FIXME dynamic channel num
        self.learnable_linear_interpolation = None

        self.camera_independent = HyVEConv(num_of_wrois=num_of_wrois,
                                           wavelength_range=self.wavelength_range,
                                           out_channels=self.hidden_layers[0],
                                           kernel_size=7,
                                           enable_extension=enable_extension,
                                           stop_gaussian_gradient=stop_gaussian_gradient
                                           )

        kernel_count = 3

        self.conv = nn.Sequential(
            nn.ReLU(True),
            nn.AvgPool2d(4),
            nn.BatchNorm2d(self.hidden_layers[0]),
            nn.Conv2d(self.hidden_layers[0], self.hidden_layers[0] * kernel_count,
                      kernel_size=3, padding=1, groups=self.hidden_layers[0]),
            nn.Conv2d(self.hidden_layers[0] * kernel_count,
                      self.hidden_layers[1], kernel_size=1),
            nn.ReLU(True),
            nn.AvgPool2d(4),
            nn.BatchNorm2d(self.hidden_layers[1]),
            nn.Conv2d(self.hidden_layers[1], self.hidden_layers[1] * kernel_count,
                      kernel_size=3, padding=1, groups=self.hidden_layers[1]),
            nn.Conv2d(self.hidden_layers[1] * kernel_count,
                      self.hidden_layers[2], kernel_size=1),
            nn.ReLU(True),
            nn.BatchNorm2d(self.hidden_layers[2]),
            nn.AdaptiveAvgPool2d((1, 1))
        )

        self.fc = nn.Sequential(
            nn.Sigmoid(),
            nn.BatchNorm1d(self.hidden_layers[2]),
            nn.Linear(self.hidden_layers[2], num_classes),
        )

        self.init_params()

    def init_params(self):
        '''Init layer parameters.'''
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_in')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, std=1e-3)
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)

    def get_hyve_conv(self):
        return self.camera_independent

    def forward(self, _x, channel_wavelengths=None):
        assert channel_wavelengths is not None

        out = self.camera_independent(_x,
                                      channel_wavelengths=channel_wavelengths)
        out = self.conv(out)
        out = out.view(_x.shape[0], -1)
        out = self.fc(out)
        return out

