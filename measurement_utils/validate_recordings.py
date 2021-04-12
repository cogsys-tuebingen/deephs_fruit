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
        return None, None

    envi_header = envi.open('%s.hdr' % path, image='%s%s' % (path, _exts))
    envi_data = envi_header.load()
    return envi_header, envi_data


def load_cube(path):
    _raw_envi_header, _raw_envi_data = load_envi(path)

    _white_envi_header, _white_envi_data = load_envi(path + "_White")
    _dark_envi_header, _dark_envi_data = load_envi(path + "_Dark")

    if _white_envi_header is None or _dark_envi_header is None:
        print("# There are no reference files, is the data already referenced?")
        return _raw_envi_data

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

    for file_path in tqdm.tqdm(file_list):
        data = load_cube(file_path)
        file_name = os.path.basename(file_path)
        data = torch.from_numpy(np.array(data).transpose(2, 0, 1))

        result, _ = func([data, None])

        # plot random spectra

        f, (ax1, ax2) = plt.subplots(1, 2)
        #ax1.xlabel("Wellenlänge")
        #ax1.ylabel("Intensität (Reflektanz)")

        spectra = data.reshape(len(wavelengths), -1).transpose(1, 0)
        idx = np.random.choice(list(range(len(spectra))), size=30)

        for _c, _s in enumerate(spectra[idx]):
            ax1.plot(wavelengths, _s)

        ax1.set_ylim([-0.1, 1])

        ax2.imshow(result.permute(1, 2, 0))
        plt.title(file_name.capitalize())
        plt.savefig(os.path.join("/tmp/imgs", "%s.png" % file_name))
#        mng = plt.get_current_fig_manager()
        #mng.resize(*mng.window.maxsize())
 #       plt.show()
