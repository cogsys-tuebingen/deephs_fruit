import argparse
import core.name_convention as name_convention


def define_parser(_description):
    parser = argparse.ArgumentParser(_description)
    return parser


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def str2cameratype(v):
    if isinstance(v, name_convention.CameraType):
        return v
    if v.lower() == 'vis':
        return name_convention.CameraType.VIS
    elif v.lower() == 'nir':
        return name_convention.CameraType.NIR
    elif v.lower() == 'rgb':
        return name_convention.CameraType.RGB
    else:
        raise argparse.ArgumentTypeError('VIS, NIR or RGB expected')


def str2fruit(v):
    if isinstance(v, name_convention.Fruit):
        return v
    if v.lower() == 'avocado':
        return name_convention.Fruit.AVOCADO
    elif v.lower() == 'kiwi':
        return name_convention.Fruit.KIWI
    else:
        raise argparse.ArgumentTypeError('AVOCADO or KIWI expected')


def str2side(v):
    if isinstance(v, name_convention.Side):
        return v
    if v.lower() == 'front':
        return name_convention.Side.FRONT
    elif v.lower() == 'back':
        return name_convention.Side.BACK
    else:
        raise argparse.ArgumentTypeError('FRONT or BACK expected')


def str2id(v):
    if isinstance(v, name_convention.ID):
        return v

    return name_convention.ID("%02i" % int(v))


def str2classification_type(v):
    if isinstance(v, name_convention.ClassificationType):
        return v

    if v.lower() == name_convention.ClassificationType.RIPENESS.value:
        return name_convention.ClassificationType.RIPENESS

    if v.lower() == name_convention.ClassificationType.FIRMNESS.value:
        return name_convention.ClassificationType.FIRMNESS

    if v.lower() == name_convention.ClassificationType.SUGAR.value:
        return name_convention.ClassificationType.SUGAR

    return name_convention.ID("%02i" % int(v))