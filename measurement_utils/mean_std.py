from core.fruit_list import *
from core.name_convention import *
import tqdm
import argparse


parser = argparse.ArgumentParser("Calculate the mean and the std over the whole dataset.")
parser.add_argument("--path", type=str, required=True)
opt = parser.parse_args()

for camera_type in CameraType:
    if camera_type == CameraType.RGB:
        # ignore the rgb recordings
        continue

    print(f"##{camera_type}")

    records = get_for_camera_type(all_fruits, camera_type)

    means = []
    stds = []

    # FIXME: use the whole dataset for std and mean
    for r in tqdm.tqdm(np.random.choice(records, 300, replace=False)):
        _, data = r.load(opt.path, is_already_referenced=True)

        data = data.reshape(-1, data.shape[2])
        means.append(data.mean(0))
        stds.append(data.std(0))
    print(f"\tMean: {np.array(means).mean(0).tolist()}")
    print(f"\tStd: {np.array(stds).mean(0)}")