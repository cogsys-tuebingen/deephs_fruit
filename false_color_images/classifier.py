import torch.nn as nn


class ClassifierModel(nn.Module):
    def __init__(self, autoencoder, bands):
        super(ClassifierModel, self).__init__()
        self.bands = bands


        self.conv = nn.Sequential(
            nn.Conv2d(3, 3, 3),
            nn.AvgPool2d(5),
            nn.ReLU(True),
        )

        self.fc = nn.Sequential(
            nn.Linear(432, 128),
            nn.ReLU(True),
            nn.Linear(128, 3)
        )

        self.init_params(self.conv)
        self.init_params(self.fc)

        self.autoencoder = autoencoder

    def init_params(self, module):
        '''Init layer parameters.'''
        for m in module:
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

    def parameters(self):
        return list(super().parameters()) + list(self.autoencoder.parameters())

    def forward(self, _x):
        batch_size, ch, w, h = _x.shape
        out = _x.permute(0, 2, 3, 1).reshape(-1, ch)
        out = self.autoencoder.encode(out)
        out = out.reshape(batch_size, w, h, 3)

        # import matplotlib.pyplot as plt
        # plt.figure()
        # plt.imshow(out.cpu().detach()[0][:, :, :])
        # plt.show()
        #
        out = out.permute(0, 3, 1, 2)

        out = self.conv(out)
        out = out.view(batch_size, -1)
        out = self.fc(out)
        return out
