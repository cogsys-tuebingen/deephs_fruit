import torch.nn as nn


class ClassifierNetwork(nn.Module):
    def __init__(self, bands, num_classes=3, hidden_layers=[25, 30, 50]):
        super(ClassifierNetwork, self).__init__()
        self.bands = bands
        kernel_count = 3
        assert len(hidden_layers) == 3

        self.conv = nn.Sequential(
            nn.Conv2d(bands, bands * kernel_count, kernel_size=7, padding=1, groups=bands),
            nn.Conv2d(bands * kernel_count, hidden_layers[0], kernel_size=1),
            nn.ReLU(True),
            nn.AvgPool2d(4),
            nn.BatchNorm2d(hidden_layers[0]),
            nn.Conv2d(hidden_layers[0], hidden_layers[0] * kernel_count, kernel_size=3, padding=1, groups=hidden_layers[0]),
            nn.Conv2d(hidden_layers[0] * kernel_count, hidden_layers[1], kernel_size=1),
            nn.ReLU(True),
            nn.AvgPool2d(4),
            nn.BatchNorm2d(hidden_layers[1]),
            nn.Conv2d(hidden_layers[1], hidden_layers[1] * kernel_count, kernel_size=3, padding=1, groups=hidden_layers[1]),
            nn.Conv2d(hidden_layers[1] * kernel_count, hidden_layers[2], kernel_size=1),
            nn.ReLU(True),
            nn.BatchNorm2d(hidden_layers[2]),
            nn.AdaptiveAvgPool2d((1, 1))
        )

        self.fc = nn.Sequential(
            nn.Sigmoid(),
            nn.BatchNorm1d(hidden_layers[2]),
            nn.Linear(hidden_layers[2], num_classes),
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

    def forward(self, _x, channel_wavelengths=None):
        out = self.conv(_x)
        out = out.view(_x.shape[0], -1)
        out = self.fc(out)
        return out
