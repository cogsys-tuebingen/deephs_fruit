from core.name_convention import *

"""
removed the RGB recordings
"""


def get_for_camera_type(_l, _camera_type: CameraType):
    _r = []
    for _e in _l:
        if _e.camera_type == _camera_type:
            _r.append(_e)

    return _r


def get_for_fruit(_l, _fruit: Fruit):
    _r = []

    if _fruit == Fruit.ALL:
        return _l

    for _e in _l:
        if _e.fruit == _fruit:
            _r.append(_e)

    return _r


def get_for_side(_l, _side: Side):
    _r = []
    for _e in _l:
        if _e.side == _side:
            _r.append(_e)

    return _r


def get_labeled_fruits(_l):
    _r = []
    for _e in _l:
        if _e.is_labeled():
            _r.append(_e)

    return _r


def get_fruits_with_state(_l, _ripeness_state: RipenessState):
    _r = []
    for _e in get_labeled_fruits(_l):
        if _e.label.ripeness_state == _ripeness_state:
            _r.append(_e)

    return _r


def get_fruits_with_adjusted_state(_l, _ripeness_state: RipenessState, _as_state: RipenessState):
    _r = []
    for _e in get_labeled_fruits(_l):
        if _e.label.ripeness_state == _ripeness_state:
            _e.label.ripeness_state = _as_state
            _r.append(_e)

    return _r


def get_fruits_with_firmness_level(_l, _level: FirmnessLevel):
    _r = []
    for _e in get_labeled_fruits(_l):
        if _e.label.firmness is None:
            continue

        if _e.label.get_firmness_level() == _level:
            _r.append(_e)

    return _r


def get_fruits_with_sugar_level(_l, _level: SugarLevel):
    _r = []
    for _e in get_labeled_fruits(_l):
        if _e.label.sugar_content is None:
            continue

        if _e.label.get_sugar_level() == _level:
            _r.append(_e)

    return _r


def get_dataset(r: FruitRecord):
    from core.measurements.val_set_fruits import val_set_fruits
    from core.measurements.test_set_fruits import test_set_fruits

    if r in test_set_fruits:
        return DATASET_TYPE.TEST
    if r in val_set_fruits:
        return DATASET_TYPE.VAL

    return DATASET_TYPE.TRAIN


def extract_test_data(records):
    rest_set = []
    test_set = []

    for _l in records:
        if get_dataset(_l) == DATASET_TYPE.TEST:
            test_set.append(_l)
        else:
            rest_set.append(_l)

    print("Test set size: %i" % len(test_set))

    return rest_set, test_set


def extract_val_data(records):
    train_set = []
    val_set = []

    for _l in records:
        if get_dataset(_l) == DATASET_TYPE.VAL:
            val_set.append(_l)
        else:
            train_set.append(_l)

    print("Val set size: %i" % len(val_set))
    print("Train set size: %i" % len(train_set))

    return train_set, val_set


def create_day_list(last_day_entries, new_day):
    entries = []

    for e in last_day_entries:
        if e.is_labeled():
            # Labeled fruit are destroyed
            continue

        entries.append(
            "FruitRecord(Fruit.{fruit}, Side.{side}, Day.{day}, "
            "ID.{id}, CameraType.{camera_type})".format(
                fruit=e.fruit.name, side=e.side.name, day=new_day.name, id=e.id.name,
                camera_type=e.camera_type.name
            ))
    print("%s = [%s]" % ("%s_all_fruits" % new_day.value, ",".join(entries)))


def to_json(records):
    import datetime
    import core.util as util

    j = {
        'info': {
            'createdAt': datetime.datetime.now().isoformat(),
        },
        'cameras': [
            {'id': 'VIS', 'name': 'Specim FX10', 'wavelengths': util.get_wavelengths_for(CameraType.VIS)},
            {'id': 'NIR', 'name': 'INNOSPEC RedEye', 'wavelengths': util.get_wavelengths_for(CameraType.NIR)},
            {'id': 'VIS_COR', 'name': 'Corning microHSI 410 Vis-NIR Hyperspectral Sensor', 'wavelengths': util.get_wavelengths_for(CameraType.VIS_COR)}
        ],
        'days': [
            {'id': 'day_01', 'date': '2019-11-04T00:00:00+0000'},
            {'id': 'day_02', 'date': '2019-11-05T00:00:00+0000'},
            {'id': 'day_03', 'date': '2019-11-06T00:00:00+0000'},
            {'id': 'day_04', 'date': '2019-11-07T00:00:00+0000'},
            {'id': 'day_05', 'date': '2019-11-08T00:00:00+0000'},
            {'id': 'day_06', 'date': '2019-11-09T00:00:00+0000'},
            {'id': 'day_07', 'date': '2019-11-10T00:00:00+0000'},
            {'id': 'day_08', 'date': '2019-11-11T00:00:00+0000'},
            {'id': 'day_09', 'date': '2019-11-12T00:00:00+0000'},
            {'id': 'day_10', 'date': '2019-11-13T00:00:00+0000'},
            {'id': 'day_11', 'date': '2019-11-14T00:00:00+0000'},
            {'id': 'day_m2_01', 'date': '2020-11-30T00:00:00+0000'},
            {'id': 'day_m2_02', 'date': '2020-12-01T00:00:00+0000'},
            {'id': 'day_m2_03', 'date': '2020-12-02T00:00:00+0000'},
            {'id': 'day_m2_04', 'date': '2020-12-03T00:00:00+0000'},
            {'id': 'day_m2_05', 'date': '2020-12-04T00:00:00+0000'},
            {'id': 'day_m2_06', 'date': '2020-12-05T00:00:00+0000'},
            {'id': 'day_m2_07', 'date': '2020-12-07T00:00:00+0000'},
            {'id': 'day_m2_08', 'date': '2020-12-08T00:00:00+0000'},
            {'id': 'day_m2_09', 'date': '2020-12-09T00:00:00+0000'},
            {'id': 'day_m2_10', 'date': '2020-12-10T00:00:00+0000'},
            {'id': 'day_m2_11', 'date': '2020-12-11T00:00:00+0000'},
            {'id': 'day_m2_12', 'date': '2020-12-12T00:00:00+0000'},
            {'id': 'day_m2_13', 'date': '2020-12-14T00:00:00+0000'},
            {'id': 'day_m2_14', 'date': '2020-12-15T00:00:00+0000'},
            {'id': 'day_m2_15', 'date': '2020-12-16T00:00:00+0000'},
            {'id': 'day_m2_16', 'date': '2020-12-17T00:00:00+0000'},
            {'id': 'day_m2_17', 'date': '2020-12-18T00:00:00+0000'},

            {'id': 'day_1_m3', 'date':  '2021-06-01T00:00:00+0000'},
            {'id': 'day_2_m3', 'date':  '2021-06-02T00:00:00+0000'},
            {'id': 'day_3_m3', 'date':  '2021-06-03T00:00:00+0000'},
            {'id': 'day_4_m3', 'date':  '2021-06-04T00:00:00+0000'},
            {'id': 'day_5_m3', 'date':  '2021-06-05T00:00:00+0000'},
            {'id': 'day_6_m3', 'date':  '2021-06-07T00:00:00+0000'},
            {'id': 'day_7_m3', 'date':  '2021-06-08T00:00:00+0000'},
            {'id': 'day_8_m3', 'date':  '2021-06-09T00:00:00+0000'},
            {'id': 'day_9_m3', 'date':  '2021-06-10T00:00:00+0000'},
            {'id': 'day_10_m3', 'date': '2021-06-11T00:00:00+0000'},
            {'id': 'day_11_m3', 'date': '2021-06-12T00:00:00+0000'},
            {'id': 'day_12_m3', 'date': '2021-06-14T00:00:00+0000'},

            {'id': 'day_m4_01', 'date': '2022-04-27T00:00:00+0000'},
            {'id': 'day_m4_02', 'date': '2022-04-28T00:00:00+0000'},
            {'id': 'day_m4_03', 'date': '2022-04-29T00:00:00+0000'},
            {'id': 'day_m4_04', 'date': '2022-04-30T00:00:00+0000'},
            {'id': 'day_m4_05', 'date': '2022-05-02T00:00:00+0000'},
            {'id': 'day_m4_06', 'date': '2022-05-03T00:00:00+0000'},
            {'id': 'day_m4_07', 'date': '2022-05-04T00:00:00+0000'},
            {'id': 'day_m4_08', 'date': '2022-05-05T00:00:00+0000'},
            {'id': 'day_m4_09', 'date': '2022-05-06T00:00:00+0000'},
        ],
        'records': [],
        'annotations': [],
    }

    # create records
    record_id = 0
    record_id_map = {}
    for r in records:
        r_j = {'id': record_id,
               'fruit': r.fruit.value,
               'side': r.side.value,
               'day': r.day.value,
               'camera_type': r.camera_type.value,
               'files':
                   {
                       'header_file': "%s.hdr" % r.get_file_path(),
                       'data_file': "%s.bin" % r.get_file_path()
                   }

               }
        j['records'].append(r_j)

        record_id_map[r] = record_id

        record_id += 1

    # create annotations
    annot_id = 0
    for r in get_labeled_fruits(records):
        a_j = {'id': annot_id,
               'record_id': record_id_map[r],
               'init_weight': r.label.init_weight,
               'end_weight': r.label.end_weight,
               'storage_days': r.label.storage_days,
               'firmness': r.label.firmness,
               'comment': r.label.comment,
               }

        if isinstance(r.label, SweetFruitLabel):
            a_j['sugar_content']= r.label.sugar_content

        if r.label.ripeness_state == RipenessState.NEAR_OVERRIPE:
            rs = RipenessState.OVERRIPE
        elif r.label.ripeness_state == RipenessState.RIPE:
            rs = RipenessState.PERFECT
        else:
            rs = r.label.ripeness_state
        a_j['ripeness_state'] = rs.value
        a_j['ripeness_state_fine'] = r.label.ripeness_state.value

        j['annotations'].append(a_j)

        annot_id += 1

    return j


if __name__ == '__main__':
    # create_day_list(day_m2_16_all_fruits, Day.DAY_M2_17)
    import json
    from core.measurements import all_fruits_new

    rest, test = extract_test_data(all_fruits_new)
    train, val = extract_val_data(rest)
    json.dump(to_json(test), open("dataset/test_v2.json", "w+"))
    json.dump(to_json(val), open("dataset/val_v2.json", "w+"))
    json.dump(to_json(get_labeled_fruits(train)), open("dataset/train_only_labeled_v2.json", "w+"))
    json.dump(to_json(train), open("dataset/train_all_v2.json", "w+"))
