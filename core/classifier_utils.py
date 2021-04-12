from core.name_convention import *


def bands_as_first_dimension(_obj):
    return _obj.transpose((2, 0, 1))


def bands_as_first_dimension_rev(_obj):
    return _obj.transpose((1, 2, 0))


def add_border(_obj):
    enlarged = np.zeros((_obj.shape[0] + 2, _obj.shape[1] + 2, _obj.shape[2]), dtype=np.float32)
    enlarged[1:-1, 1:-1] = -_obj
    return enlarged
