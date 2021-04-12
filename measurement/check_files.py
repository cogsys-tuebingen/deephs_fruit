import argparse
import core.argparser_utils as argparser_utils
import tqdm
from core.fruit_list import *
from core.name_convention import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser("This script visualize the hyperspectral recordings of a directory"
                                     " to validate whether the measurements are usable.")
    parser.add_argument("--path", type=str, required=True)
    parser.add_argument("--camera_type", type=argparser_utils.str2cameratype, required=True)
    opt = parser.parse_args()

    # TODO: adapt
    records = day_m2_17_all_fruits

    wavelengths = util.get_wavelengths_for(opt.camera_type)

    for r in tqdm.tqdm(records):
        r.load(opt.path, is_already_referenced=False)

    print("Could find all required files.")