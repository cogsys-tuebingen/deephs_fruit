import numpy as np
import cv2 as cv
from core.name_convention import *


def extract_obj_by_mask(_mask, _envi_data, _remove_background_pixels=True):
    """
    :param _mask:
    :param _envi_data:
    :param _remove_background_pixels

    :return: a list of all found objects
    """
    # mask should be a grayscale image between 0-255
    _mask = np.uint8(255 * _mask)

    # now find the contours in the image
    ctrs, hier = cv.findContours(_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    boundingRects = [cv.boundingRect(cv.approxPolyDP(c, 3, True)) for c in ctrs]

    # the last step is now two find the rectangles for each obj
    _objects = []
    for (x, y, size_x, size_y) in boundingRects:
        # exclude too small objects and the whole image
        if size_x * size_y < 100 * 100 or (x == 0 and y == 0):
            continue

        _data = _envi_data

        if _remove_background_pixels:
            _data = np.array(_data).copy()
            _data = _data.reshape(-1, _data.shape[2])
            _data[(_mask.reshape(-1, 1) == 0)[:, 0]] = np.zeros(_data.shape[1])
            _data = _data.reshape(_envi_data.shape[0], _envi_data.shape[1], _envi_data.shape[2])

        cv.rectangle(_mask, (x, y), (x + size_x, y + size_y), (50), 2)
        _objects.append(_data[y:y + size_y, x:x + size_x])

    return _objects


def scale_to(_obj, _width, _height):
    _obj = cv.resize(_obj, dsize=(_width, _height), interpolation=cv.INTER_CUBIC)
    return _obj


def exists(fruit: FruitRecord, output_path: str):
    name = fruit.get_file_path()

    return os.path.exists(os.path.join(output_path, "%s.hdr" % name))


def store_object(_fruit: FruitRecord, _obj, output_path: str):
    _name = _fruit.get_file_path()

    _export_name = os.path.join(output_path, _name)
    spectral_io.save_envi(_export_name, _obj, force=True)


def extract(data_path, output_path, all_records, camera_type, model):
    import torch
    import tqdm

    with torch.no_grad():
        for r in tqdm.tqdm(all_records, desc="Extract the fruits"):
            if exists(r, output_path):
                continue

            envi_header, envi_data_referenced = r.load(data_path)

            w, h = envi_data_referenced.shape[:2]

            pixels = envi_data_referenced.reshape((-1, len(util.get_wavelengths_for(camera_type))))
            mask_pixels = model(torch.from_numpy(pixels)).argmax(1).detach()
            mask = mask_pixels.reshape(w, h)
            fruit_crop = extract_obj_by_mask(mask, envi_data_referenced, True)

            assert len(fruit_crop) == 1  # there should be only one fruit in the recording
            fruit_crop = fruit_crop[0]

            if r.side == Side.BACK:
                # all fruits should be upside down
                fruit_crop = np.flip(fruit_crop, axis=0)

            store_object(r, fruit_crop, output_path)


if __name__ == '__main__':
    from core.fruit_list import *
    from extract_fruit.train import LayerClassifierModule

    camera_type = CameraType.VIS
    fruit = Fruit.AVOCADO
    all_records = get_for_camera_type(get_for_fruit(all_fruits, fruit), camera_type)
    best_model = LayerClassifierModule.load_from_checkpoint(all_records=all_records,
                                                            checkpoint_path="/home/lvarga/repository/DeepHS/publish/extract_fruit/_ckpt_epoch_103_v1.ckpt")
    extract("/data/measurements/Messung_whole/", "/data/measurements/extracted_fruit", all_records,
            camera_type, best_model)
