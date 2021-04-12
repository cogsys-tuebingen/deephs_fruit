import argparse
import core.argparser_utils as argparser_utils
import tqdm
from core.fruit_list import *
from core.hyperspectral_dataset import prepare_fruit

if __name__ == '__main__':
    parser = argparse.ArgumentParser("This script visualize the hyperspectral recordings of a directory"
                                     " to validate whether the measurements are usable.")
    parser.add_argument("--fruit", type=argparser_utils.str2fruit, required=True)
    parser.add_argument("--number", type=int, required=True)
    opt = parser.parse_args()

    # TODO: adapt
    records = day_m2_16_all_fruits
    records = get_for_fruit(records, opt.fruit)
    records = get_for_side(records, Side.FRONT)

    selected = np.random.choice(records, opt.number)

    print([f.id.value for f in selected])
