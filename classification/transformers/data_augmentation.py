import torch
import math
import numpy as np
from core.name_convention import *

AUGMENTATION_CONFIG = {
    'random_flip': True,
    'random_rotate': True,
    'random_noise': False,
    'random_cut': True
}


class Augmenter(object):
    def __init__(self, classification_type: ClassificationType, augmentation_config: dict):
        self.classification_type = classification_type
        self.augmentation_config = augmentation_config

    def _random_flip(self, _t: torch.Tensor):
        d = np.random.randint(0, 4)

        if d == 0:
            return _t
        if d == 1:
            return _t.flip(1)
        if d == 2:
            return _t.flip(2)
        if d == 3:
            return _t.flip([1, 2])

    def _random_noise(self, _t: torch.Tensor):
        _n = torch.normal(0, 1e-1, _t.shape)
        return _t + _n

    def _random_noise_v2(self, _t: torch.Tensor):
        ch, h, w = _t.shape

        _std = _t.std((1, 2)).expand(h, w, ch).permute(2, 0, 1)
        _mean = _t.mean((1, 2)).expand(h, w, ch).permute(2, 0, 1)

        _n = torch.normal(_mean, _std)
        return _t + (0.8 * _n)

    def _cut_off(self, _t: torch.Tensor):
        _cut_off_size = 16
        _center_cut_off = np.random.randint(0, 64, 2)
        _x_0 = int(max(_center_cut_off[0] - (_cut_off_size / 2), 0))
        _y_0 = int(max(_center_cut_off[1] - (_cut_off_size / 2), 0))
        _x_1 = int(min(_center_cut_off[0] + (_cut_off_size / 2), 63))
        _y_1 = int(min(_center_cut_off[1] + (_cut_off_size / 2), 63))

        _t[:, _x_0:_x_1, _y_0:_y_1] = 0
        return _t

    def _nearest_interp2d(self, input, coords):
        """
        2d nearest neighbor interpolation th.Tensor
        """
        # take clamp of coords so they're in the image bounds
        x = torch.clamp(coords[:, :, 0], 0, input.size(1) - 1).round()
        y = torch.clamp(coords[:, :, 1], 0, input.size(2) - 1).round()

        stride = torch.LongTensor(input.stride())
        x_ix = x.mul(stride[1]).long()
        y_ix = y.mul(stride[2]).long()

        input_flat = input.view(input.size(0), -1)

        mapped_vals = input_flat.gather(1, x_ix.add(y_ix))

        return mapped_vals.view_as(input)

    def _bilinear_interp2d(self, input, coords):
        """
        bilinear interpolation in 2d
        """
        x = torch.clamp(coords[:, :, 0], 0, input.size(1) - 2)
        x0 = x.floor()
        x1 = x0 + 1
        y = torch.clamp(coords[:, :, 1], 0, input.size(2) - 2)
        y0 = y.floor()
        y1 = y0 + 1

        stride = torch.LongTensor(input.stride())
        x0_ix = x0.mul(stride[1]).long()
        x1_ix = x1.mul(stride[1]).long()
        y0_ix = y0.mul(stride[2]).long()
        y1_ix = y1.mul(stride[2]).long()

        input_flat = input.view(input.size(0), -1)

        vals_00 = input_flat.gather(1, x0_ix.add(y0_ix))
        vals_10 = input_flat.gather(1, x1_ix.add(y0_ix))
        vals_01 = input_flat.gather(1, x0_ix.add(y1_ix))
        vals_11 = input_flat.gather(1, x1_ix.add(y1_ix))

        xd = x - x0
        yd = y - y0
        xm = 1 - xd
        ym = 1 - yd

        x_mapped = (vals_00.mul(xm).mul(ym) +
                    vals_10.mul(xd).mul(ym) +
                    vals_01.mul(xm).mul(yd) +
                    vals_11.mul(xd).mul(yd))

        return x_mapped.view_as(input)

    def _iterproduct(self, *args):
        return torch.from_numpy(np.indices(args).reshape((len(args), -1)).T)

    def _affine2d(self, x, matrix, mode='bilinear', center=True):
        """
        2D Affine image transform on torch.Tensor

        Arguments
        ---------
        x : torch.Tensor of size (C, H, W)
            image tensor to be transformed
        matrix : torch.Tensor of size (3, 3) or (2, 3)
            transformation matrix
        mode : string in {'nearest', 'bilinear'}
            interpolation scheme to use
        center : boolean
            whether to alter the bias of the transform
            so the transform is applied about the center
            of the image rather than the origin
        Example
        -------
                >>> import torch
                >>> x = torch.zeros(2,1000,1000)
                >>> x[:,100:1500,100:500] = 10
                >>> matrix = torch.FloatTensor([[1.,0,-50],
                ...                             [0,1.,-50]])
                >>> xn = _affine2d(x, matrix, mode='nearest')
                >>> xb = _affine2d(x, matrix, mode='bilinear')
        """

        if matrix.dim() == 2:
            matrix = matrix[:2, :]
            matrix = matrix.unsqueeze(0)
        elif matrix.dim() == 3:
            if matrix.size()[1:] == (3, 3):
                matrix = matrix[:, :2, :]

        A_batch = matrix[:, :, :2]
        if A_batch.size(0) != x.size(0):
            A_batch = A_batch.repeat(x.size(0), 1, 1)
        b_batch = matrix[:, :, 2].unsqueeze(1)

        # make a meshgrid of normal coordinates
        _coords = self._iterproduct(x.size(1), x.size(2))
        coords = _coords.unsqueeze(0).repeat(x.size(0), 1, 1).float().to(x.device)

        if center:
            # shift the coordinates so center is the origin
            coords[:, :, 0] = coords[:, :, 0] - (x.size(1) / 2. - 0.5)
            coords[:, :, 1] = coords[:, :, 1] - (x.size(2) / 2. - 0.5)
        # apply the coordinate transformation
        new_coords = coords.bmm(A_batch.transpose(1, 2)) + b_batch.expand_as(coords)

        if center:
            # shift the coordinates back so origin is origin
            new_coords[:, :, 0] = new_coords[:, :, 0] + (x.size(1) / 2. - 0.5)
            new_coords[:, :, 1] = new_coords[:, :, 1] + (x.size(2) / 2. - 0.5)

        # map new coordinates using bilinear interpolation
        if mode == 'nearest':
            x_transformed = self._nearest_interp2d(x.contiguous(), new_coords)
        elif mode == 'bilinear':
            x_transformed = self._bilinear_interp2d(x.contiguous(), new_coords)

        return x_transformed

    def _random_rotate(self, _i):
        """
        rotates between -45° and 45°

        :param _i:
        :return:
        """

        random_degree = np.random.randint(-90, 90)

        theta = math.pi / 180 * random_degree
        rotation_matrix = torch.tensor(
            [[math.cos(theta), -math.sin(theta), 0],
             [math.sin(theta), math.cos(theta), 0],
             [0, 0, 1]], dtype=torch.float32).to(_i.device)
        input_tf = self._affine2d(_i,
                                  rotation_matrix,
                                  center=True,
                                  mode='nearest')
        return input_tf

    def _random_cut(self, x, ratio=1 / 2):
        h, w = x.shape[1:]

        cut_w = int(w * ratio)
        cut_h = int(h * ratio)

        pos_x = np.random.randint(0 - cut_w, w)
        pos_y = np.random.randint(0 - cut_h, h)

        x = x.clone()
        x[:, max(0, pos_x):min(w, pos_x + cut_w), max(0, pos_y):min(h, pos_y + cut_h)] = 0

        return x

    def __call__(self, batch):
        x, y = batch

        if self.augmentation_config['random_flip']:
            x = self._random_flip(x)
        if self.augmentation_config['random_rotate']:
            x = self._random_rotate(x)
        if self.augmentation_config['random_noise']:
            x = self._random_noise_v2(x)
        if self.augmentation_config['random_cut']:
            x = self._random_cut(x)

        return x, y
