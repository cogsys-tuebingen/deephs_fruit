import torch
from classification.transformers.to_rgb import ToRGB
import glob
import argparse
import core.argparser_utils as argparser_utils
import os
import spectral
import spectral.io.envi as envi
import core.spectral_io as spectral_io
import numpy as np
import tqdm
import matplotlib.pyplot as plt
import core.util as util


def load_envi(path):
    _exts = '.bin'
    if not os.path.exists('%s%s' % (path, _exts)):
        _exts = '.img'

    if not os.path.exists('%s%s' % (path, _exts)):
        raise spectral.io.spyfile.FileNotFoundError("Could not find data for: %s" % path)

    envi_header = envi.open('%s.hdr' % path, image='%s%s' % (path, _exts))
    envi_data = envi_header.load()
    return envi_header, envi_data


def load_cube(path):
    _raw_envi_header, _raw_envi_data = load_envi(path)
    _white_envi_header, _white_envi_data = load_envi(path + "_White")
    _dark_envi_header, _dark_envi_data = load_envi(path + "_Dark")

    return spectral_io.use_references(_raw_envi_data, _white_envi_data, _dark_envi_data)


def get_file_list(folder):
    list_of_files = glob.glob(os.path.join(folder, "*.hdr"))

    # remove the white and dark references
    main_files = list(filter(lambda x: not (x.endswith("_White.hdr") or x.endswith("_Dark.hdr")), list_of_files))

    # remove the .hdr ending
    main_files = list(map(lambda x: x.replace(".hdr", ""), main_files))
    return main_files


if __name__ == '__main__':
    parser = argparse.ArgumentParser("This script visualize the hyperspectral recordings of a directory"
                                     " to validate whether the measurements are usable.")
    parser.add_argument("--path", type=str, required=True)
    parser.add_argument("--camera_type", type=argparser_utils.str2cameratype, required=True)
    opt = parser.parse_args()

    func = ToRGB(opt.camera_type)
    file_list = get_file_list(opt.path)

    wavelengths = util.get_wavelengths_for(opt.camera_type)

    for file_path in tqdm.tqdm(file_list, desc="Create rgb images"):
        data = load_cube(file_path)
        file_name = os.path.basename(file_path)
        data = torch.from_numpy(np.array(data).transpose(2, 0, 1))

        result, _ = func([data, None])

        folder = os.path.join("/tmp", "rgb_images")
        if not os.path.exists(folder):
            os.mkdir(folder)

        result = result.permute(1, 2, 0).numpy()

        plt.imsave(fname=os.path.join(folder, "%s.png" % file_name), arr=result)
