from torch import nn

"""
 This is layer classifier
 Learns to mask the object
"""


class LayerClassifierModel(nn.Module):
    def __init__(self, _bands):
        super(LayerClassifierModel, self).__init__()
        self.bands = _bands

        self.layers = nn.Sequential(
            nn.Linear(self.bands, 300),
            nn.ReLU(inplace=True),
            nn.Linear(300, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, 64),
            nn.ReLU(inplace=True),
            nn.Linear(64, 32),
            nn.ReLU(inplace=True),
            nn.Linear(32, 2)
        )

    def forward(self, _input):
        return self.layers(_input)