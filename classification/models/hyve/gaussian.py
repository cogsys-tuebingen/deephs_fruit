import numpy as np

import torch
import torch.nn as nn


class GaussDistributionModule(nn.Module):
    def __init__(self, gauss_num, mean_bias, mean_range, variance_factor, equally_distributed=True):
        super().__init__()
        self.gauss_num = gauss_num
        self.equally_distributed = equally_distributed

        self.mean = torch.zeros(self.gauss_num)
        self.stdev = torch.zeros(self.gauss_num)
        self.mean = nn.parameter.Parameter(self.mean)
        self.stdev = nn.parameter.Parameter(self.stdev)

        self.variance_factor = variance_factor
        self.mean_bias = mean_bias
        self.mean_range = mean_range
        # SoftPlus always larger than 0 -> "A Comprehensive guide to
        # Bayesian Convolutional Neural Network with Variational Inference"
        self.softplus = nn.Softplus()
        self.initialize_weights()

    def initialize_weights(self):
        mean = torch.linspace(
            0, 1, self.gauss_num + 2)[1:-1] if self.equally_distributed \
            else torch.rand(self.gauss_num)
        stdev = torch.tensor([1 / (self.gauss_num) for _ in range(self.gauss_num)]) \
            if self.equally_distributed \
            else torch.rand(self.gauss_num)
        self.mean = nn.parameter.Parameter(mean)
        self.stdev = nn.parameter.Parameter(stdev)

    def scaled_params(self):
        mean = self.mean_bias + self.mean_range * self.mean
        variance = torch.pow(self.softplus(self.stdev),
                             2) * self.variance_factor

        return mean, variance

    def forward(self, x):
        if isinstance(x, list):
            x = torch.tensor(x)

        if not isinstance(x, torch.Tensor):
            x = torch.from_numpy(x)

        if len(x.shape) < 2:
            x = x.unsqueeze(-1)

        mean, variance = self.scaled_params()

        return (1 / torch.sqrt(2 * np.pi * variance) * torch.exp(-torch.pow(x - mean, 2) / (2 * variance)))
