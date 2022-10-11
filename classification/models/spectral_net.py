import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import math

def WaveletTransformAxisY(batch_img):
    odd_img  = batch_img[:,0::2]
    even_img = batch_img[:,1::2]
    L = (odd_img + even_img) / 2.0
    H = (odd_img - even_img).abs()
    return L, H

def WaveletTransformAxisX(batch_img):
    # transpose + fliplr
    tmp_batch = batch_img.permute(0, 2, 1).flip(2)
    _dst_L, _dst_H = WaveletTransformAxisY(tmp_batch)
    # transpose + flipud
    dst_L = _dst_L.permute(0, 2, 1).flip(1)
    dst_H = _dst_H.permute(0, 2, 1).flip(1)
    return dst_L, dst_H

def Wavelet(batch_image):
    # make channel first image
    batch_image = batch_image
    channels = batch_image.shape[1]

    # level 1 decomposition
    wavelet_data = []
    wavelet_LLs = []
    for channel in range(channels):
        d = batch_image[:, channel]

        wavelet_L, wavelet_H = WaveletTransformAxisY(d)
        wavelet_LL, wavelet_LH = WaveletTransformAxisX(wavelet_L)
        wavelet_HL, wavelet_HH = WaveletTransformAxisX(wavelet_H)

        wavelet_data += [wavelet_LL, wavelet_LH, wavelet_HL, wavelet_HH]
        wavelet_LLs.append(wavelet_LL)

    transform_batch = torch.stack(wavelet_data, axis=1)

    # level 2 decomposition
    wavelet_data_l2 = []
    wavelet_LL2s = []
    for channel in range(channels):
        wavelet_L2, wavelet_H2 = WaveletTransformAxisY(wavelet_LLs[channel])
        wavelet_LL2, wavelet_LH2 = WaveletTransformAxisX(wavelet_L2)
        wavelet_HL2, wavelet_HH2 = WaveletTransformAxisX(wavelet_H2)

        wavelet_data_l2 += [wavelet_LL2, wavelet_LH2, wavelet_HL2, wavelet_HH2]
        wavelet_LL2s.append(wavelet_LL2)

    transform_batch_l2 = torch.stack(wavelet_data_l2, axis=1)

    # level 3 decomposition
    wavelet_data_l3 = []
    wavelet_LL3s = []
    for channel in range(channels):
        wavelet_L3, wavelet_H3 = WaveletTransformAxisY(wavelet_LL2s[channel])
        wavelet_LL3, wavelet_LH3 = WaveletTransformAxisX(wavelet_L3)
        wavelet_HL3, wavelet_HH3 = WaveletTransformAxisX(wavelet_H3)

        wavelet_data_l3 += [wavelet_LL3, wavelet_LH3, wavelet_HL3, wavelet_HH3]
        wavelet_LL3s.append(wavelet_LL3)

    transform_batch_l3 = torch.stack(wavelet_data_l3, axis=1)

    # level 4 decomposition
    wavelet_data_l4 = []
    for channel in range(channels):
        wavelet_L4, wavelet_H4 = WaveletTransformAxisY(wavelet_LL3s[channel])
        wavelet_LL4, wavelet_LH4 = WaveletTransformAxisX(wavelet_L4)
        wavelet_HL4, wavelet_HH4 = WaveletTransformAxisX(wavelet_H4)

        wavelet_data_l4 += [wavelet_LL4, wavelet_LH4, wavelet_HL4, wavelet_HH4]

    transform_batch_l4 = torch.stack(wavelet_data_l4, axis=1)

    decom_level_1 = transform_batch
    decom_level_2 = transform_batch_l2
    decom_level_3 = transform_batch_l3
    decom_level_4 = transform_batch_l4

    return [decom_level_1, decom_level_2, decom_level_3, decom_level_4]

def WaveletRGB(batch_image):
    assert batch_image.shape[1] == 3
    # make channel first image
    batch_image = batch_image
    r = batch_image[:,0]
    g = batch_image[:,1]
    b = batch_image[:,2]

    # level 1 decomposition
    wavelet_L, wavelet_H = WaveletTransformAxisY(r)
    r_wavelet_LL, r_wavelet_LH = WaveletTransformAxisX(wavelet_L)
    r_wavelet_HL, r_wavelet_HH = WaveletTransformAxisX(wavelet_H)

    wavelet_L, wavelet_H = WaveletTransformAxisY(g)
    g_wavelet_LL, g_wavelet_LH = WaveletTransformAxisX(wavelet_L)
    g_wavelet_HL, g_wavelet_HH = WaveletTransformAxisX(wavelet_H)

    wavelet_L, wavelet_H = WaveletTransformAxisY(b)
    b_wavelet_LL, b_wavelet_LH = WaveletTransformAxisX(wavelet_L)
    b_wavelet_HL, b_wavelet_HH = WaveletTransformAxisX(wavelet_H)

    wavelet_data = [r_wavelet_LL, r_wavelet_LH, r_wavelet_HL, r_wavelet_HH,
                    g_wavelet_LL, g_wavelet_LH, g_wavelet_HL, g_wavelet_HH,
                    b_wavelet_LL, b_wavelet_LH, b_wavelet_HL, b_wavelet_HH]
    transform_batch = torch.stack(wavelet_data, axis=1)

    # level 2 decomposition
    wavelet_L2, wavelet_H2 = WaveletTransformAxisY(r_wavelet_LL)
    r_wavelet_LL2, r_wavelet_LH2 = WaveletTransformAxisX(wavelet_L2)
    r_wavelet_HL2, r_wavelet_HH2 = WaveletTransformAxisX(wavelet_H2)

    wavelet_L2, wavelet_H2 = WaveletTransformAxisY(g_wavelet_LL)
    g_wavelet_LL2, g_wavelet_LH2 = WaveletTransformAxisX(wavelet_L2)
    g_wavelet_HL2, g_wavelet_HH2 = WaveletTransformAxisX(wavelet_H2)

    wavelet_L2, wavelet_H2 = WaveletTransformAxisY(b_wavelet_LL)
    b_wavelet_LL2, b_wavelet_LH2 = WaveletTransformAxisX(wavelet_L2)
    b_wavelet_HL2, b_wavelet_HH2 = WaveletTransformAxisX(wavelet_H2)


    wavelet_data_l2 = [r_wavelet_LL2, r_wavelet_LH2, r_wavelet_HL2, r_wavelet_HH2,
                    g_wavelet_LL2, g_wavelet_LH2, g_wavelet_HL2, g_wavelet_HH2,
                    b_wavelet_LL2, b_wavelet_LH2, b_wavelet_HL2, b_wavelet_HH2]
    transform_batch_l2 = torch.stack(wavelet_data_l2, axis=1)

    # level 3 decomposition
    wavelet_L3, wavelet_H3 = WaveletTransformAxisY(r_wavelet_LL2)
    r_wavelet_LL3, r_wavelet_LH3 = WaveletTransformAxisX(wavelet_L3)
    r_wavelet_HL3, r_wavelet_HH3 = WaveletTransformAxisX(wavelet_H3)

    wavelet_L3, wavelet_H3 = WaveletTransformAxisY(g_wavelet_LL2)
    g_wavelet_LL3, g_wavelet_LH3 = WaveletTransformAxisX(wavelet_L3)
    g_wavelet_HL3, g_wavelet_HH3 = WaveletTransformAxisX(wavelet_H3)

    wavelet_L3, wavelet_H3 = WaveletTransformAxisY(b_wavelet_LL2)
    b_wavelet_LL3, b_wavelet_LH3 = WaveletTransformAxisX(wavelet_L3)
    b_wavelet_HL3, b_wavelet_HH3 = WaveletTransformAxisX(wavelet_H3)

    wavelet_data_l3 = [r_wavelet_LL3, r_wavelet_LH3, r_wavelet_HL3, r_wavelet_HH3,
                    g_wavelet_LL3, g_wavelet_LH3, g_wavelet_HL3, g_wavelet_HH3,
                    b_wavelet_LL3, b_wavelet_LH3, b_wavelet_HL3, b_wavelet_HH3]
    transform_batch_l3 = torch.stack(wavelet_data_l3, axis=1)

    # level 4 decomposition
    wavelet_L4, wavelet_H4 = WaveletTransformAxisY(r_wavelet_LL3)
    r_wavelet_LL4, r_wavelet_LH4 = WaveletTransformAxisX(wavelet_L4)
    r_wavelet_HL4, r_wavelet_HH4 = WaveletTransformAxisX(wavelet_H4)

    wavelet_L4, wavelet_H4 = WaveletTransformAxisY(g_wavelet_LL3)
    g_wavelet_LL4, g_wavelet_LH4 = WaveletTransformAxisX(wavelet_L4)
    g_wavelet_HL4, g_wavelet_HH4 = WaveletTransformAxisX(wavelet_H4)

    wavelet_L3, wavelet_H3 = WaveletTransformAxisY(b_wavelet_LL3)
    b_wavelet_LL4, b_wavelet_LH4 = WaveletTransformAxisX(wavelet_L4)
    b_wavelet_HL4, b_wavelet_HH4 = WaveletTransformAxisX(wavelet_H4)


    wavelet_data_l4 = [r_wavelet_LL4, r_wavelet_LH4, r_wavelet_HL4, r_wavelet_HH4,
                    g_wavelet_LL4, g_wavelet_LH4, g_wavelet_HL4, g_wavelet_HH4,
                    b_wavelet_LL4, b_wavelet_LH4, b_wavelet_HL4, b_wavelet_HH4]
    transform_batch_l4 = torch.stack(wavelet_data_l4, axis=1)

    decom_level_1 = transform_batch
    decom_level_2 = transform_batch_l2
    decom_level_3 = transform_batch_l3
    decom_level_4 = transform_batch_l4

    return [decom_level_1, decom_level_2, decom_level_3, decom_level_4]

class Conv2dSame(nn.Conv2d):

    def calc_same_pad(self, i: int, k: int, s: int, d: int) -> int:
        return max((math.ceil(i / s) - 1) * s + (k - 1) * d + 1 - i, 0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        ih, iw = x.size()[-2:]

        pad_h = self.calc_same_pad(i=ih, k=self.kernel_size[0], s=self.stride[0], d=self.dilation[0])
        pad_w = self.calc_same_pad(i=iw, k=self.kernel_size[1], s=self.stride[1], d=self.dilation[1])

        if pad_h > 0 or pad_w > 0:
            x = F.pad(
                x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2]
            )
        return F.conv2d(
            x,
            self.weight,
            self.bias,
            self.stride,
            self.padding,
            self.dilation,
            self.groups,
        )


class SpectralNet(nn.Module):
    def __init__(self, bands, num_classes):
        super(SpectralNet, self).__init__()
        self.bands = bands
        self.num_classes = num_classes

        self.wavelet = Wavelet

        self.relu = nn.ReLU()
        layer_1_chin = bands * 4
        layer_2_chin = layer_1_chin
        layer_3_chin = layer_1_chin
        layer_4_chin = layer_1_chin

        self.conv_1 = Conv2dSame(layer_1_chin, 64, kernel_size=(3, 3))
        self.norm_1 = nn.BatchNorm2d(64)
        self.conv_1_2 = Conv2dSame(64, 64, kernel_size=(3, 3), stride=2)
        self.norm_1_2 = nn.BatchNorm2d(64)

        self.conv_a = Conv2dSame(layer_2_chin, 64, kernel_size=(3, 3))
        self.norm_a = nn.BatchNorm2d(64)

        self.conv_2 = Conv2dSame(128, 128, kernel_size=(3, 3))
        self.norm_2 = nn.BatchNorm2d(128)
        self.conv_2_2 = Conv2dSame(128, 128, kernel_size=(3, 3), stride=2)
        self.norm_2_2 = nn.BatchNorm2d(128)

        self.conv_b = Conv2dSame(layer_3_chin, 64, kernel_size=(3, 3))
        self.norm_b = nn.BatchNorm2d(64)
        self.conv_b_2 = Conv2dSame(64, 128, kernel_size=(3, 3))
        self.norm_b_2 = nn.BatchNorm2d(128)

        self.conv_3 = Conv2dSame(256, 256, kernel_size=(3, 3))
        self.norm_3 = nn.BatchNorm2d(256)
        self.conv_3_2 = Conv2dSame(256, 256, kernel_size=(3, 3), stride=2)
        self.norm_3_2 = nn.BatchNorm2d(256)

        self.conv_c = Conv2dSame(layer_4_chin, 64, kernel_size=(3, 3))
        self.norm_c = nn.BatchNorm2d(64)
        self.conv_c_2 = Conv2dSame(64, 128, kernel_size=(3, 3))
        self.norm_c_2 = nn.BatchNorm2d(128)
        self.conv_c_3 = Conv2dSame(128, 256, kernel_size=(3, 3))
        self.norm_c_3 = nn.BatchNorm2d(256)

        self.conv_4 = Conv2dSame(512, 256, kernel_size=(3, 3))
        self.norm_4 = nn.BatchNorm2d(256)
        self.conv_4_2 = Conv2dSame(256, 256, kernel_size=(3, 3), stride=2)
        self.norm_4_2 = nn.BatchNorm2d(256)

        self.conv_5 = Conv2dSame(256, 128, kernel_size=(3, 3))
        self.norm_5 = nn.BatchNorm2d(128)

        self.pool = nn.AdaptiveAvgPool2d(1)

        self.dense1 = nn.Linear(128, 2048)
        self.dense1_do = nn.Dropout(0.4)
        self.dense2 = nn.Linear(2048, 1024)
        self.dense2_do = nn.Dropout(0.4)
        self.output_layer = nn.Linear(1024, self.num_classes)
        self.softmax = nn.Softmax()

    def forward(self, x, channel_wavelengths):
        input_l1, input_l2, input_l3, input_l4 = self.wavelet(x)

        # level one decomposition starts
        x_1 = self.conv_1(input_l1)
        x_1 = self.norm_1(x_1)
        x_1 = self.relu(x_1)
        x_1 = self.conv_1_2(x_1)
        x_1 = self.norm_1_2(x_1)
        x_1 = self.relu(x_1)

        # level two decomposition starts
        x_2 = self.conv_a(input_l2)
        x_2 = self.norm_a(x_2)
        x_2 = self.relu(x_2)
        # concate level one and level two decomposition
        c_2 = torch.cat([x_1, x_2], axis=1)
        c_2 = self.conv_2(c_2)
        c_2 = self.norm_2(c_2)
        c_2 = self.relu(c_2)
        c_2 = self.conv_2_2(c_2)
        c_2 = self.norm_2_2(c_2)
        c_2 = self.relu(c_2)
        
        # level three decomposition starts
        x_3 = self.conv_b(input_l3)
        x_3 = self.norm_b(x_3)
        x_3 = self.relu(x_3)
        x_3 = self.conv_b_2(x_3)
        x_3 = self.norm_b_2(x_3)
        x_3 = self.relu(x_3)
        # concate level one and level two decomposition
        c_3 = torch.cat([c_2, x_3], axis=1)
        c_3 = self.conv_3(c_3)
        c_3 = self.norm_3(c_3)
        c_3 = self.relu(c_3)
        c_3 = self.conv_3_2(c_3)
        c_3 = self.norm_3_2(c_3)
        c_3 = self.relu(c_3)

        # level four decomposition starts
        x_4 = self.conv_c(input_l4)
        x_4 = self.norm_c(x_4)
        x_4 = self.relu(x_4)
        x_4 = self.conv_c_2(x_4)
        x_4 = self.norm_c_2(x_4)
        x_4 = self.relu(x_4)
        x_4 = self.conv_c_3(x_4)
        x_4 = self.norm_c_3(x_4)
        x_4 = self.relu(x_4)

        # concate level level three and level four decomposition
        c_4 = torch.cat([c_3, x_4], axis=1)
        c_4 = self.conv_4(c_4)
        c_4 = self.norm_4(c_4)
        c_4 = self.relu(c_4)
        c_4 = self.conv_4_2(c_4)
        c_4 = self.norm_4_2(c_4)
        c_4 = self.relu(c_4)


        c_5 = self.conv_5(c_4)
        c_5 = self.norm_5(c_5)
        c_5 = self.relu(c_5)

        pooled = self.pool(c_5)
        flat = pooled.view(pooled.shape[0], -1)
        out = self.dense1(flat)
        out = self.relu(out)
        out = self.dense1_do(out)
        out = self.dense2(out)
        out = self.relu(out)
        out = self.dense2_do(out)
        out = self.output_layer(out)
        out = self.softmax(out)

        return out

if __name__ == '__main__':
    img_batch = torch.zeros((8, 3, 24, 24))

    for i in range(4):
        print(Wavelet(img_batch)[i].shape)
        print(WaveletRGB(img_batch)[i].shape)

    model = SpectralNet(3, 16)
    print(model(img_batch, None))


