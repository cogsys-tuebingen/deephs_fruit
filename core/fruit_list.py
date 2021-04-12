from core.name_convention import *
import numpy as np

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


def get_all_for_a_fruit(_fruit: Fruit, _id: ID, _side: Side, _camera_type: CameraType, _use_better_set=False):
    _r = []
    _label = None

    if _use_better_set:
        dataset = all_fruits_m1_better
    else:
        dataset = all_fruits_m1

    for _e in dataset:
        if _e.fruit == _fruit and _e.id == _id and _e.side == _side and _e.camera_type == _camera_type:
            _r.append(_e)

            if _e.is_labeled():
                _label = _e.label

    return _r, _label


test_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),
]

test_all_vis_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.TEST_1, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.VIS),
]

test_all_nir_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.TEST_2, ID.UNKNOWN, CameraType.NIR),
]

day_1_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_3, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_3, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_3, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_3, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_20, CameraType.NIR,
                AvocadoLabel(227, 227, 0, 19750, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_20, CameraType.VIS,
                AvocadoLabel(227, 227, 0, 19750, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_20, CameraType.NIR,
                AvocadoLabel(227, 227, 0, 19750, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_20, CameraType.VIS,
                AvocadoLabel(227, 227, 0, 19750, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_30, CameraType.NIR,
                AvocadoLabel(252, 252, 0, 18250, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_1, ID.ID_30, CameraType.VIS,
                AvocadoLabel(252, 252, 0, 18250, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_30, CameraType.NIR,
                AvocadoLabel(252, 252, 0, 18250, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_1, ID.ID_30, CameraType.VIS,
                AvocadoLabel(252, 252, 0, 18250, RipenessState.UNRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_3, CameraType.NIR,
                KiwiLabel(120, 120, 0, 900, 16.2, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_3, CameraType.VIS,
                KiwiLabel(120, 120, 0, 900, 16.2, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_3, CameraType.NIR,
                KiwiLabel(120, 120, 0, 900, 16.2, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_3, CameraType.VIS,
                KiwiLabel(120, 120, 0, 900, 16.2, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_28, CameraType.NIR,
                KiwiLabel(114, 114, 0, 900, 17.5, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_28, CameraType.VIS,
                KiwiLabel(114, 114, 0, 900, 17.5, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_28, CameraType.NIR,
                KiwiLabel(114, 114, 0, 900, 17.5, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_28, CameraType.VIS,
                KiwiLabel(114, 114, 0, 900, 17.5, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_30, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_30, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_30, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_30, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_31, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_31, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_31, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_31, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_32, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_32, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_32, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_32, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_33, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_33, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_33, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_33, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_37, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_37, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_37, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_37, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_38, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_38, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_39, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_1, ID.ID_39, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_39, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_1, ID.ID_39, CameraType.VIS),
]

day_2_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_3, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_3, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_3, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_3, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_9, CameraType.NIR,
                AvocadoLabel(183, 180, 1, 2100, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_9, CameraType.VIS,
                AvocadoLabel(183, 180, 1, 2100, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_9, CameraType.NIR,
                AvocadoLabel(183, 180, 1, 2100, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_9, CameraType.VIS,
                AvocadoLabel(183, 180, 1, 2100, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_26, CameraType.NIR,
                AvocadoLabel(245, 242, 1, 21000, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_26, CameraType.VIS,
                AvocadoLabel(245, 242, 1, 21000, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_26, CameraType.NIR,
                AvocadoLabel(245, 242, 1, 21000, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_26, CameraType.VIS,
                AvocadoLabel(245, 242, 1, 21000, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_2, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_2, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_10, CameraType.NIR,
                KiwiLabel(121, 120, 1, 1150, 16.35, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_10, CameraType.VIS,
                KiwiLabel(121, 120, 1, 1150, 16.35, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_10, CameraType.NIR,
                KiwiLabel(121, 120, 1, 1150, 16.35, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_10, CameraType.VIS,
                KiwiLabel(121, 120, 1, 1150, 16.35, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_15, CameraType.NIR,
                KiwiLabel(120, 119, 1, 1350, 16.25, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_15, CameraType.VIS,
                KiwiLabel(120, 119, 1, 1350, 16.25, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_15, CameraType.NIR,
                KiwiLabel(120, 119, 1, 1350, 16.25, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_15, CameraType.VIS,
                KiwiLabel(120, 119, 1, 1350, 16.25, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_17, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_17, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_30, CameraType.NIR,
                KiwiLabel(131, 130, 1, 1550, 14.85, RipenessState.UNRIPE, "Near ripe")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_30, CameraType.VIS,
                KiwiLabel(131, 130, 1, 1550, 14.85, RipenessState.UNRIPE, "Near ripe")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_30, CameraType.NIR,
                KiwiLabel(131, 130, 1, 1550, 14.85, RipenessState.UNRIPE, "Near ripe")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_30, CameraType.VIS,
                KiwiLabel(131, 130, 1, 1550, 14.85, RipenessState.UNRIPE, "Near ripe")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_31, CameraType.NIR,
                KiwiLabel(128, 127, 1, 1375, 15, RipenessState.UNRIPE, "Near ripe")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_31, CameraType.VIS,
                KiwiLabel(128, 127, 1, 1375, 15, RipenessState.UNRIPE, "Near ripe")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_31, CameraType.NIR,
                KiwiLabel(128, 127, 1, 1375, 15, RipenessState.UNRIPE, "Near ripe")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_31, CameraType.VIS,
                KiwiLabel(128, 127, 1, 1375, 15, RipenessState.UNRIPE, "Near ripe")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_32, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_32, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_32, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_32, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_33, CameraType.NIR,
                KiwiLabel(133, 132, 1, 0, 15, RipenessState.OVERRIPE, "Damaged")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_33, CameraType.VIS,
                KiwiLabel(133, 132, 1, 0, 15, RipenessState.OVERRIPE, "Damaged")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_33, CameraType.NIR,
                KiwiLabel(133, 132, 1, 0, 15, RipenessState.OVERRIPE, "Damaged")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_33, CameraType.VIS,
                KiwiLabel(133, 132, 1, 0, 15, RipenessState.OVERRIPE, "Damaged")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_37, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_37, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_37, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_37, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_38, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_38, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_39, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_2, ID.ID_39, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_39, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_2, ID.ID_39, CameraType.VIS)]

day_3_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_3, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_3, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_3, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_3, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_5, CameraType.NIR,
                AvocadoLabel(231, 224, 2, 1200, RipenessState.RIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_5, CameraType.VIS,
                AvocadoLabel(231, 224, 2, 1200, RipenessState.RIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_5, CameraType.NIR,
                AvocadoLabel(231, 224, 2, 1200, RipenessState.RIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_5, CameraType.VIS,
                AvocadoLabel(231, 224, 2, 1200, RipenessState.RIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_13, CameraType.NIR,
                AvocadoLabel(240, 231, 2, 4450, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_13, CameraType.VIS,
                AvocadoLabel(240, 231, 2, 4450, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_13, CameraType.NIR,
                AvocadoLabel(240, 231, 2, 4450, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_13, CameraType.VIS,
                AvocadoLabel(240, 231, 2, 4450, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_15, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_15, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_17, CameraType.NIR,
                AvocadoLabel(242, 235, 2, 4650, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_17, CameraType.VIS,
                AvocadoLabel(242, 235, 2, 4650, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_17, CameraType.NIR,
                AvocadoLabel(242, 235, 2, 4650, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_17, CameraType.VIS,
                AvocadoLabel(242, 235, 2, 4650, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_23, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_23, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_5, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_5, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_7, CameraType.NIR,
                KiwiLabel(123, 121, 2, 150, 17.25, RipenessState.OVERRIPE, "Could be also ripe")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_7, CameraType.VIS,
                KiwiLabel(123, 121, 2, 150, 17.25, RipenessState.OVERRIPE, "Could be also ripe")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_7, CameraType.NIR,
                KiwiLabel(123, 121, 2, 150, 17.25, RipenessState.OVERRIPE, "Could be also ripe")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_7, CameraType.VIS,
                KiwiLabel(123, 121, 2, 150, 17.25, RipenessState.OVERRIPE, "Could be also ripe")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_8, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_8, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_12, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_12, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_13, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_13, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_17, CameraType.NIR,
                KiwiLabel(117, 115, 2, 1050, 17, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_17, CameraType.VIS,
                KiwiLabel(117, 115, 2, 1050, 17, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_17, CameraType.NIR,
                KiwiLabel(117, 115, 2, 1050, 17, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_17, CameraType.VIS,
                KiwiLabel(117, 115, 2, 1050, 17, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_18, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_18, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_19, CameraType.NIR,
                KiwiLabel(133, 131, 2, 2200, 15.5, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_19, CameraType.VIS,
                KiwiLabel(133, 131, 2, 2200, 15.5, RipenessState.UNRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_19, CameraType.NIR,
                KiwiLabel(133, 131, 2, 2200, 15.5, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_19, CameraType.VIS,
                KiwiLabel(133, 131, 2, 2200, 15.5, RipenessState.UNRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_23, CameraType.NIR,
                KiwiLabel(127, 126, 2, 1750, 16, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_23, CameraType.VIS,
                KiwiLabel(127, 126, 2, 1750, 16, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_23, CameraType.NIR,
                KiwiLabel(127, 126, 2, 1750, 16, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_23, CameraType.VIS,
                KiwiLabel(127, 126, 2, 1750, 16, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_26, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_26, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_32, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_32, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_32, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_32, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_37, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_37, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_37, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_37, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_38, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_38, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_39, CameraType.NIR,
                KiwiLabel(132, 131, 2, 2400, 16.25, RipenessState.UNRIPE, "Could be also ripe")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_39, CameraType.VIS,
                KiwiLabel(132, 131, 2, 2400, 16.25, RipenessState.UNRIPE, "Could be also ripe")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_39, CameraType.NIR,
                KiwiLabel(132, 131, 2, 2400, 16.25, RipenessState.UNRIPE, "Could be also ripe")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_39, CameraType.VIS,
                KiwiLabel(132, 131, 2, 2400, 16.25, RipenessState.UNRIPE, "Could be also ripe")),
]

day_4_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_1, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_1, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_1, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_1, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_2, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_2, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_2, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_2, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_3, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_3, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_3, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_3, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_4, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_4, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_4, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_4, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_6, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_6, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_6, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_6, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_7, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_7, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_7, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_7, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_8, CameraType.NIR,
                                AvocadoLabel(253, 244, 3, 1300, RipenessState.RIPE)),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_8, CameraType.VIS,
                                AvocadoLabel(253, 244, 3, 1300, RipenessState.RIPE)),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_8, CameraType.NIR,
                                AvocadoLabel(253, 244, 3, 1300, RipenessState.RIPE)),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_8, CameraType.VIS,
                                AvocadoLabel(253, 244, 3, 1300, RipenessState.RIPE)),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_10, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_10, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_10, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_10, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_11, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_11, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_11, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_11, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_12, CameraType.NIR,
                                AvocadoLabel(229, 216, 3, 750, RipenessState.PERFECT)),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_12, CameraType.VIS,
                                AvocadoLabel(229, 216, 3, 750, RipenessState.PERFECT)),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_12, CameraType.NIR,
                                AvocadoLabel(229, 216, 3, 750, RipenessState.PERFECT)),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_12, CameraType.VIS,
                                AvocadoLabel(229, 216, 3, 750, RipenessState.PERFECT)),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_14, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_14, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_14, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_14, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_15, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_15, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_15, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_15, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_16, CameraType.NIR,
                                AvocadoLabel(232, 222, 3, 1200, RipenessState.PERFECT)),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_16, CameraType.VIS,
                                AvocadoLabel(232, 222, 3, 1200, RipenessState.PERFECT)),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_16, CameraType.NIR,
                                AvocadoLabel(232, 222, 3, 1200, RipenessState.PERFECT)),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_16, CameraType.VIS,
                                AvocadoLabel(232, 222, 3, 1200, RipenessState.PERFECT)),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_18, CameraType.NIR,
                                AvocadoLabel(246, 233, 3, 1000, RipenessState.PERFECT)),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_18, CameraType.VIS,
                                AvocadoLabel(246, 233, 3, 1000, RipenessState.PERFECT)),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_18, CameraType.NIR,
                                AvocadoLabel(246, 233, 3, 1000, RipenessState.PERFECT)),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_18, CameraType.VIS,
                                AvocadoLabel(246, 233, 3, 1000, RipenessState.PERFECT)),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_19, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_19, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_19, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_19, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_21, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_21, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_21, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_21, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_22, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_22, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_22, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_22, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_23, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_23, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_23, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_23, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_24, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_24, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_24, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_24, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_25, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_25, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_25, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_25, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_27, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_27, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_27, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_27, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_28, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_28, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_28, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_28, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_29, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_4, ID.ID_29, CameraType.VIS),

                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_29, CameraType.NIR),
                    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_29, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_1, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_1, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_1, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_1, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_2, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_2, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_2, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_2, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_4, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_4, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_4, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_4, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_5, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_5, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_5, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_5, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_6, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_6, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_6, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_6, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_8, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_8, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_8, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_8, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_9, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_9, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_9, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_9, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_11, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_11, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_11, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_11, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_12, CameraType.NIR,
                                KiwiLabel(124, 122, 3, 1150, 17.5, RipenessState.PERFECT)),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_12, CameraType.VIS,
                                KiwiLabel(124, 122, 3, 1150, 17.5, RipenessState.PERFECT)),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_12, CameraType.NIR,
                                KiwiLabel(124, 122, 3, 1150, 17.5, RipenessState.PERFECT)),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_12, CameraType.VIS,
                                KiwiLabel(124, 122, 3, 1150, 17.5, RipenessState.PERFECT)),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_13, CameraType.NIR,
                                KiwiLabel(120, 117, 3, 800, 18, RipenessState.NEAR_OVERRIPE)),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_13, CameraType.VIS,
                                KiwiLabel(120, 117, 3, 800, 18, RipenessState.NEAR_OVERRIPE)),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_13, CameraType.NIR,
                                KiwiLabel(120, 117, 3, 800, 18, RipenessState.NEAR_OVERRIPE)),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_13, CameraType.VIS,
                                KiwiLabel(120, 117, 3, 800, 18, RipenessState.NEAR_OVERRIPE)),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_14, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_14, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_14, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_14, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_16, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_16, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_16, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_16, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_18, CameraType.NIR,
                                KiwiLabel(133, 132, 3, 2050, 16, RipenessState.UNRIPE, "no comment")),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_18, CameraType.VIS,
                                KiwiLabel(133, 132, 3, 2050, 16, RipenessState.UNRIPE, "no comment")),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_18, CameraType.NIR,
                                KiwiLabel(133, 132, 3, 2050, 16, RipenessState.UNRIPE, "no comment")),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_18, CameraType.VIS,
                                KiwiLabel(133, 132, 3, 2050, 16, RipenessState.UNRIPE, "no comment")),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_20, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_20, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_20, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_20, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_21, CameraType.NIR,
                                KiwiLabel(125, 123, 3, 1450, 15, RipenessState.RIPE)),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_21, CameraType.VIS,
                                KiwiLabel(125, 123, 3, 1450, 15, RipenessState.RIPE)),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_21, CameraType.NIR,
                                KiwiLabel(125, 123, 3, 1450, 15, RipenessState.RIPE)),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_21, CameraType.VIS,
                                KiwiLabel(125, 123, 3, 1450, 15, RipenessState.RIPE)),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_22, CameraType.NIR,
                                KiwiLabel(127, 124, 3, 1000, 16.7, RipenessState.OVERRIPE, "Damaged")),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_22, CameraType.VIS,
                                KiwiLabel(127, 124, 3, 1000, 16.7, RipenessState.OVERRIPE, "Damaged")),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_22, CameraType.NIR,
                                KiwiLabel(127, 124, 3, 1000, 16.7, RipenessState.OVERRIPE, "Damaged")),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_22, CameraType.VIS,
                                KiwiLabel(127, 124, 3, 1000, 16.7, RipenessState.OVERRIPE, "Damaged")),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_24, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_24, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_24, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_24, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_25, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_25, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_25, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_25, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_26, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_26, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_26, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_26, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_27, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_27, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_27, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_27, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_29, CameraType.NIR,
                                KiwiLabel(132, 130, 3, 1950, 16, RipenessState.RIPE)),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_29, CameraType.VIS,
                                KiwiLabel(132, 130, 3, 1950, 16, RipenessState.RIPE)),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_29, CameraType.NIR,
                                KiwiLabel(132, 130, 3, 1950, 16, RipenessState.RIPE)),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_29, CameraType.VIS,
                                KiwiLabel(132, 130, 3, 1950, 16, RipenessState.RIPE)),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_32, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_32, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_32, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_32, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_34, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_34, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_34, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_34, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_35, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_35, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_35, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_35, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_36, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_36, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_36, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_36, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_37, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_37, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_37, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_37, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_38, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_38, CameraType.VIS),

                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_38, CameraType.NIR),
                    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_38, CameraType.VIS),

                    ]

day_5_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_3, CameraType.NIR,
                AvocadoLabel(247, 232, 4, 5100, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_3, CameraType.VIS,
                AvocadoLabel(247, 232, 4, 5100, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_3, CameraType.NIR,
                AvocadoLabel(247, 232, 4, 5100, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_3, CameraType.VIS,
                AvocadoLabel(247, 232, 4, 5100, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_14, CameraType.NIR,
                AvocadoLabel(241, 223, 4, 900, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_14, CameraType.VIS,
                AvocadoLabel(241, 223, 4, 900, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_14, CameraType.NIR,
                AvocadoLabel(241, 223, 4, 900, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_14, CameraType.VIS,
                AvocadoLabel(241, 223, 4, 900, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_15, CameraType.NIR,
                AvocadoLabel(233, 217, 4, 1000, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_15, CameraType.VIS,
                AvocadoLabel(233, 217, 4, 1000, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_15, CameraType.NIR,
                AvocadoLabel(233, 217, 4, 1000, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_15, CameraType.VIS,
                AvocadoLabel(233, 217, 4, 1000, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_19, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_19, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_21, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_21, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_23, CameraType.NIR,
                AvocadoLabel(243, 232, 4, 14500, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_23, CameraType.VIS,
                AvocadoLabel(243, 232, 4, 14500, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_23, CameraType.NIR,
                AvocadoLabel(243, 232, 4, 14500, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_23, CameraType.VIS,
                AvocadoLabel(243, 232, 4, 14500, RipenessState.UNRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_2, CameraType.NIR,
                KiwiLabel(117, 115, 4, 1400, 17.25, RipenessState.PERFECT, "no comment")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_2, CameraType.VIS,
                KiwiLabel(117, 115, 4, 1400, 17.25, RipenessState.PERFECT, "no comment")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_2, CameraType.NIR,
                KiwiLabel(117, 115, 4, 1400, 17.25, RipenessState.PERFECT, "no comment")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_2, CameraType.VIS,
                KiwiLabel(117, 115, 4, 1400, 17.25, RipenessState.PERFECT, "no comment")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_5, CameraType.NIR,
                KiwiLabel(119, 117, 4, 1200, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_5, CameraType.VIS,
                KiwiLabel(119, 117, 4, 1200, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_5, CameraType.NIR,
                KiwiLabel(119, 117, 4, 1200, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_5, CameraType.VIS,
                KiwiLabel(119, 117, 4, 1200, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_8, CameraType.NIR,
                KiwiLabel(124, 122, 4, 1700, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_8, CameraType.VIS,
                KiwiLabel(124, 122, 4, 1700, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_8, CameraType.NIR,
                KiwiLabel(124, 122, 4, 1700, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_8, CameraType.VIS,
                KiwiLabel(124, 122, 4, 1700, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_20, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_20, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_26, CameraType.NIR,
                KiwiLabel(135, 133, 4, 1650, 16, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_26, CameraType.VIS,
                KiwiLabel(135, 133, 4, 1650, 16, RipenessState.UNRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_26, CameraType.NIR,
                KiwiLabel(135, 133, 4, 1650, 16, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_26, CameraType.VIS,
                KiwiLabel(135, 133, 4, 1650, 16, RipenessState.UNRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_32, CameraType.NIR,
                KiwiLabel(125, 123, 4, 1500, 15.5, RipenessState.UNRIPE, "near ripe")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_32, CameraType.VIS,
                KiwiLabel(125, 123, 4, 1500, 15.5, RipenessState.UNRIPE, "near ripe")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_32, CameraType.NIR,
                KiwiLabel(125, 123, 4, 1500, 15.5, RipenessState.UNRIPE, "near ripe")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_32, CameraType.VIS,
                KiwiLabel(125, 123, 4, 1500, 15.5, RipenessState.UNRIPE, "near ripe")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_35, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_35, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_36, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_36, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_37, CameraType.NIR,
                KiwiLabel(129, 127, 4, 1750, 15, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_37, CameraType.VIS,
                KiwiLabel(129, 127, 4, 1750, 15, RipenessState.UNRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_37, CameraType.NIR,
                KiwiLabel(129, 127, 4, 1750, 15, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_37, CameraType.VIS,
                KiwiLabel(129, 127, 4, 1750, 15, RipenessState.UNRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_38, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_38, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_38, CameraType.VIS),

]

day_6_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_2, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_2, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_6, CameraType.NIR,
                AvocadoLabel(234, 215, 5, 900, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_6, CameraType.VIS,
                AvocadoLabel(234, 215, 5, 900, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_6, CameraType.NIR,
                AvocadoLabel(234, 215, 5, 900, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_6, CameraType.VIS,
                AvocadoLabel(234, 215, 5, 900, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_11, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_11, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_19, CameraType.NIR,
                AvocadoLabel(195, 177, 5, 700, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_19, CameraType.VIS,
                AvocadoLabel(195, 177, 5, 700, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_19, CameraType.NIR,
                AvocadoLabel(195, 177, 5, 700, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_19, CameraType.VIS,
                AvocadoLabel(195, 177, 5, 700, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_21, CameraType.NIR,
                AvocadoLabel(251, 235, 5, 650, RipenessState.PERFECT, "near overripe")),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_21, CameraType.VIS,
                AvocadoLabel(251, 235, 5, 650, RipenessState.PERFECT, "near overripe")),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_21, CameraType.NIR,
                AvocadoLabel(251, 235, 5, 650, RipenessState.PERFECT, "near overripe")),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_21, CameraType.VIS,
                AvocadoLabel(251, 235, 5, 650, RipenessState.PERFECT, "near overripe")),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_25, CameraType.NIR,
                AvocadoLabel(249, 231, 5, 900, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_25, CameraType.VIS,
                AvocadoLabel(249, 231, 5, 900, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_25, CameraType.NIR,
                AvocadoLabel(249, 231, 5, 900, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_25, CameraType.VIS,
                AvocadoLabel(249, 231, 5, 900, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_1, CameraType.NIR,
                KiwiLabel(116, 114, 5, 950, 16.5, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_1, CameraType.VIS,
                KiwiLabel(116, 114, 5, 950, 16.5, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_1, CameraType.NIR,
                KiwiLabel(116, 114, 5, 950, 16.5, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_1, CameraType.VIS,
                KiwiLabel(116, 114, 5, 950, 16.5, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_6, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_6, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_9, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_9, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_11, CameraType.NIR,
                KiwiLabel(120, 116, 5, 950, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_11, CameraType.VIS,
                KiwiLabel(120, 116, 5, 950, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_11, CameraType.NIR,
                KiwiLabel(120, 116, 5, 950, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_11, CameraType.VIS,
                KiwiLabel(120, 116, 5, 950, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_14, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_14, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_16, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_16, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_20, CameraType.NIR,
                KiwiLabel(124, 121, 5, 750, 17.5, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_20, CameraType.VIS,
                KiwiLabel(124, 121, 5, 750, 17.5, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_20, CameraType.NIR,
                KiwiLabel(124, 121, 5, 750, 17.5, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_20, CameraType.VIS,
                KiwiLabel(124, 121, 5, 750, 17.5, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_35, CameraType.NIR,
                KiwiLabel(125, 123, 5, 900, 16.2, RipenessState.PERFECT, "maybe overripe")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_35, CameraType.VIS,
                KiwiLabel(125, 123, 5, 900, 16.2, RipenessState.PERFECT, "maybe overripe")),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_35, CameraType.NIR,
                KiwiLabel(125, 123, 5, 900, 16.2, RipenessState.PERFECT, "maybe overripe")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_35, CameraType.VIS,
                KiwiLabel(125, 123, 5, 900, 16.2, RipenessState.PERFECT, "maybe overripe")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_36, CameraType.NIR,
                KiwiLabel(127, 125, 5, 1500, 15, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_36, CameraType.VIS,
                KiwiLabel(127, 125, 5, 1500, 15, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_36, CameraType.NIR,
                KiwiLabel(127, 125, 5, 1500, 15, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_36, CameraType.VIS,
                KiwiLabel(127, 125, 5, 1500, 15, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_38, CameraType.NIR,
                KiwiLabel(130, 128, 5, 1750, 17, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_38, CameraType.VIS,
                KiwiLabel(130, 128, 5, 1750, 17, RipenessState.RIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_38, CameraType.NIR,
                KiwiLabel(130, 128, 5, 1750, 17, RipenessState.RIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_38, CameraType.VIS,
                KiwiLabel(130, 128, 5, 1750, 17, RipenessState.RIPE)),

]

day_7_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_2, CameraType.NIR,
                AvocadoLabel(255, 229, 7, 750, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_2, CameraType.VIS,
                AvocadoLabel(255, 229, 7, 750, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_2, CameraType.NIR,
                AvocadoLabel(255, 229, 7, 750, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_2, CameraType.VIS,
                AvocadoLabel(255, 229, 7, 750, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_10, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_10, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_11, CameraType.NIR,
                AvocadoLabel(239, 218, 7, 850, RipenessState.NEAR_OVERRIPE, 'first brown lines')),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_11, CameraType.VIS,
                AvocadoLabel(239, 218, 7, 850, RipenessState.NEAR_OVERRIPE, 'first brown lines')),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_11, CameraType.NIR,
                AvocadoLabel(239, 218, 7, 850, RipenessState.NEAR_OVERRIPE, 'first brown lines')),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_11, CameraType.VIS,
                AvocadoLabel(239, 218, 7, 850, RipenessState.NEAR_OVERRIPE, 'first brown lines')),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_27, CameraType.NIR,
                AvocadoLabel(245, 223, 7, 1050, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_27, CameraType.VIS,
                AvocadoLabel(245, 223, 7, 1050, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_27, CameraType.NIR,
                AvocadoLabel(245, 223, 7, 1050, RipenessState.PERFECT)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_27, CameraType.VIS,
                AvocadoLabel(245, 223, 7, 1050, RipenessState.PERFECT)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_28, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_28, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_6, CameraType.NIR,
                KiwiLabel(124, 121, 7, 1250, 17.8, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_6, CameraType.VIS,
                KiwiLabel(124, 121, 7, 1250, 17.8, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_6, CameraType.NIR,
                KiwiLabel(124, 121, 7, 1250, 17.8, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_6, CameraType.VIS,
                KiwiLabel(124, 121, 7, 1250, 17.8, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_9, CameraType.NIR,
                KiwiLabel(122, 119, 7, 800, 17.2, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_9, CameraType.VIS,
                KiwiLabel(122, 119, 7, 800, 17.2, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_9, CameraType.NIR,
                KiwiLabel(122, 119, 7, 800, 17.2, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_9, CameraType.VIS,
                KiwiLabel(122, 119, 7, 800, 17.2, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_14, CameraType.NIR,
                KiwiLabel(115, 110, 7, 700, 16, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_14, CameraType.VIS,
                KiwiLabel(115, 110, 7, 700, 16, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_14, CameraType.NIR,
                KiwiLabel(115, 110, 7, 700, 16, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_14, CameraType.VIS,
                KiwiLabel(115, 110, 7, 700, 16, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_16, CameraType.NIR,
                KiwiLabel(117, 114, 7, 0, 17, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_16, CameraType.VIS,
                KiwiLabel(117, 114, 7, 0, 17, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_16, CameraType.NIR,
                KiwiLabel(117, 114, 7, 0, 17, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_16, CameraType.VIS,
                KiwiLabel(117, 114, 7, 0, 17, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_24, CameraType.NIR,
                KiwiLabel(125, 122, 7, 1650, 16, RipenessState.UNRIPE, 'not really ripe is too firm')),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_24, CameraType.VIS,
                KiwiLabel(125, 122, 7, 1650, 16, RipenessState.UNRIPE, 'not really ripe is too firm')),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_24, CameraType.NIR,
                KiwiLabel(125, 122, 7, 1650, 16, RipenessState.UNRIPE, 'not really ripe is too firm')),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_24, CameraType.VIS,
                KiwiLabel(125, 122, 7, 1650, 16, RipenessState.UNRIPE, 'not really ripe is too firm')),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_34, CameraType.VIS),

]

day_8_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_10, CameraType.NIR,
                AvocadoLabel(229, 202, 8, 700, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_10, CameraType.VIS,
                AvocadoLabel(229, 202, 8, 700, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_10, CameraType.NIR,
                AvocadoLabel(229, 202, 8, 700, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_10, CameraType.VIS,
                AvocadoLabel(229, 202, 8, 700, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_22, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_22, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_28, CameraType.NIR,
                AvocadoLabel(250, 218, 8, 725, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_28, CameraType.VIS,
                AvocadoLabel(250, 218, 8, 725, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_28, CameraType.NIR,
                AvocadoLabel(250, 218, 8, 725, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_28, CameraType.VIS,
                AvocadoLabel(250, 218, 8, 725, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_29, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_29, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_4, CameraType.NIR,
                KiwiLabel(128, 123, 8, 0, 17.5, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_4, CameraType.VIS,
                KiwiLabel(128, 123, 8, 0, 17.5, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_4, CameraType.NIR,
                KiwiLabel(128, 123, 8, 0, 17.5, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_4, CameraType.VIS,
                KiwiLabel(128, 123, 8, 0, 17.5, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_25, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_25, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_8, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_34, CameraType.VIS),

]

day_9_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_1, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_1, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_7, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_7, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_22, CameraType.NIR,
                AvocadoLabel(237, 208, 9, 775, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_22, CameraType.VIS,
                AvocadoLabel(237, 208, 9, 775, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_22, CameraType.NIR,
                AvocadoLabel(237, 208, 9, 775, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_22, CameraType.VIS,
                AvocadoLabel(237, 208, 9, 775, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_24, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_24, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_29, CameraType.NIR,
                AvocadoLabel(240, 211, 9, 750, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_29, CameraType.VIS,
                AvocadoLabel(240, 211, 9, 750, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_29, CameraType.NIR,
                AvocadoLabel(240, 211, 9, 750, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_29, CameraType.VIS,
                AvocadoLabel(240, 211, 9, 750, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_9, ID.ID_25, CameraType.NIR,
                KiwiLabel(126, 120, 9, 1350, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_9, ID.ID_25, CameraType.VIS,
                KiwiLabel(126, 120, 9, 1350, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_9, ID.ID_25, CameraType.NIR,
                KiwiLabel(126, 120, 9, 1350, 16, RipenessState.PERFECT)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_9, ID.ID_25, CameraType.VIS,
                KiwiLabel(126, 120, 9, 1350, 16, RipenessState.PERFECT)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_9, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_9, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_9, ID.ID_27, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_9, ID.ID_27, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_9, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_9, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_9, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_9, ID.ID_34, CameraType.VIS),

]

day_10_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_1, CameraType.NIR,
                AvocadoLabel(228, 190, 10, 400, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_1, CameraType.VIS,
                AvocadoLabel(228, 190, 10, 400, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_1, CameraType.NIR,
                AvocadoLabel(228, 190, 10, 400, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_1, CameraType.VIS,
                AvocadoLabel(228, 190, 10, 400, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_4, CameraType.NIR),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_4, CameraType.VIS),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_7, CameraType.NIR,
                AvocadoLabel(243, 195, 10, 625, RipenessState.OVERRIPE, "maybe endweight not correct")),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_7, CameraType.VIS,
                AvocadoLabel(243, 195, 10, 625, RipenessState.OVERRIPE, "maybe endweight not correct")),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_7, CameraType.NIR,
                AvocadoLabel(243, 195, 10, 625, RipenessState.OVERRIPE, "maybe endweight not correct")),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_7, CameraType.VIS,
                AvocadoLabel(243, 195, 10, 625, RipenessState.OVERRIPE, "maybe endweight not correct")),

    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_24, CameraType.NIR,
                AvocadoLabel(253, 216, 10, 300, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_24, CameraType.VIS,
                AvocadoLabel(253, 216, 10, 300, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_24, CameraType.NIR,
                AvocadoLabel(253, 216, 10, 300, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_10, ID.ID_24, CameraType.VIS,
                AvocadoLabel(253, 216, 10, 300, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_10, ID.ID_27, CameraType.NIR,
                KiwiLabel(134, 129, 10, 800, 15, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_10, ID.ID_27, CameraType.VIS,
                KiwiLabel(134, 129, 10, 800, 15, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_10, ID.ID_27, CameraType.NIR,
                KiwiLabel(134, 129, 10, 800, 15, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_10, ID.ID_27, CameraType.VIS,
                KiwiLabel(134, 129, 10, 800, 15, RipenessState.NEAR_OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_10, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_10, ID.ID_34, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_10, ID.ID_34, CameraType.NIR),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_10, ID.ID_34, CameraType.VIS),

]

day_11_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_11, ID.ID_4, CameraType.NIR,
                AvocadoLabel(238, 197, 11, 900, RipenessState.OVERRIPE, "damaged")),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_11, ID.ID_4, CameraType.VIS,
                AvocadoLabel(238, 197, 11, 900, RipenessState.OVERRIPE, "damaged")),

    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_11, ID.ID_4, CameraType.NIR,
                AvocadoLabel(238, 197, 11, 900, RipenessState.OVERRIPE, "damaged")),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_11, ID.ID_4, CameraType.VIS,
                AvocadoLabel(238, 197, 11, 900, RipenessState.OVERRIPE, "damaged")),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_11, ID.ID_34, CameraType.NIR,
                KiwiLabel(130, 125, 11, 800, 16, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_11, ID.ID_34, CameraType.VIS,
                KiwiLabel(130, 125, 11, 800, 16, RipenessState.OVERRIPE)),

    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_11, ID.ID_34, CameraType.NIR,
                KiwiLabel(130, 125, 11, 800, 16, RipenessState.OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_11, ID.ID_34, CameraType.VIS,
                KiwiLabel(130, 125, 11, 800, 16, RipenessState.OVERRIPE)),

]

day_m2_01_all_fruits = [
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_31, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_31, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_32, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_32, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_33, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_33, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_34, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_34, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_35, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_35, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_36, CameraType.VIS),  # INIT_WEIGHT: 204
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_36, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_37, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_37, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_38, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_38, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_39, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_39, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_40, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_40, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_41, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_41, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_42, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_42, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_43, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_43, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_44, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_44, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_45, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_45, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_46, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_46, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_47, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_47, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_48, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_48, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_49, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_49, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_50, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_50, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_51, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_51, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_52, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_52, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_53, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_53, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_54, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_54, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_55, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_55, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_56, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_56, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_57, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_57, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_58, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_58, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_59, CameraType.VIS,
                AvocadoLabel(244, 244, 0, 6000, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_59, CameraType.VIS,
                AvocadoLabel(244, 244, 0, 6000, RipenessState.UNRIPE)),
    FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_1, ID.ID_60, CameraType.VIS),
    FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_1, ID.ID_60, CameraType.VIS),

    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_40, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_40, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_41, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_41, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_42, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_42, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_43, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_43, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_44, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_44, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_45, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_45, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_46, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_46, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_47, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_47, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_48, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_48, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_49, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_49, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_50, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_50, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_51, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_51, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_52, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_52, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_53, CameraType.VIS,
                KiwiLabel(88, 88, 0, 2400, 12.5, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_53, CameraType.VIS,
                KiwiLabel(88, 88, 0, 2400, 12.5, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_54, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_54, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_55, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_55, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_56, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_56, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_57, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_57, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_58, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_58, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_59, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_59, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_60, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_60, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_61, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_61, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_62, CameraType.VIS,
                KiwiLabel(104, 104, 0, 0, 17, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_62, CameraType.VIS,
                KiwiLabel(104, 104, 0, 0, 17, RipenessState.NEAR_OVERRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_63, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_63, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_64, CameraType.VIS),  # INIT_WEIGHT:122
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_64, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_65, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_65, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_66, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_66, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_67, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_67, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_68, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_68, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_69, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_69, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_70, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_70, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_71, CameraType.VIS,
                KiwiLabel(103, 103, 0, 1900, 13, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_71, CameraType.VIS,
                KiwiLabel(103, 103, 0, 1900, 13, RipenessState.UNRIPE)),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_72, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_72, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_73, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_73, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_74, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_74, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_75, CameraType.VIS,
                KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_75, CameraType.VIS,
                KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_76, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_76, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_77, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_77, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_78, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_78, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_79, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_79, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_80, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_80, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_81, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_81, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_82, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_82, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_83, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_83, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_84, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_84, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_85, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_85, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_86, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_86, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_87, CameraType.VIS),
    FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_87, CameraType.VIS),
]

day_m2_02_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_31, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_31, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_32, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_32, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_33, CameraType.VIS,
                                    AvocadoLabel(246, 150, 1, 1400, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_33, CameraType.VIS,
                                    AvocadoLabel(246, 150, 1, 1400, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_35, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_35, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_36, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_36, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_39, CameraType.VIS,
                                    AvocadoLabel(210, 146, 1, 0, RipenessState.PERFECT, "not very tasteful")),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_39, CameraType.VIS,
                                    AvocadoLabel(210, 146, 1, 0, RipenessState.PERFECT, "not very tasteful")),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_40, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_40, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_43, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_43, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_50, CameraType.VIS,
                                    AvocadoLabel(220, 146, 1, 800, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_50, CameraType.VIS,
                                    AvocadoLabel(220, 146, 1, 800, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_52, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_52, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_56, CameraType.VIS,
                                    AvocadoLabel(199, 196, 1, 750, RipenessState.RIPE, "not very tasteful")),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_56, CameraType.VIS,
                                    AvocadoLabel(199, 196, 1, 750, RipenessState.RIPE, "not very tasteful")),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_2, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_60, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_40, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_40, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_43, CameraType.VIS,
                                    KiwiLabel(106, 105, 1, 1350, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_43, CameraType.VIS,
                                    KiwiLabel(106, 105, 1, 1350, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_52, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_52, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_61, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_61, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_65, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_65, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_70, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_70, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_72, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_72, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_74, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_74, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_77, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_77, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_81, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_81, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_85, CameraType.VIS,
                                    KiwiLabel(133, 133, 1, 2425, 13, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_85, CameraType.VIS,
                                    KiwiLabel(133, 133, 1, 2425, 13, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_86, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_86, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_2, ID.ID_87, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_2, ID.ID_87, CameraType.VIS)]

day_m2_03_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_31, CameraType.VIS,
                                    AvocadoLabel(205, 197, 2, 550, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_31, CameraType.VIS,
                                    AvocadoLabel(205, 197, 2, 550, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_32, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_32, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_35, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_35, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_36, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_36, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_40, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_40, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_43, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_43, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_47, CameraType.VIS,
                                    AvocadoLabel(241, 237, 2, 1050, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_47, CameraType.VIS,
                                    AvocadoLabel(241, 237, 2, 1050, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_51, CameraType.VIS,
                                    AvocadoLabel(218, 212, 2, 625, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_51, CameraType.VIS,
                                    AvocadoLabel(218, 212, 2, 625, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_52, CameraType.VIS,
                                    AvocadoLabel(250, 244, 2, 1775, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_52, CameraType.VIS,
                                    AvocadoLabel(250, 244, 2, 1775, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_60, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_40, CameraType.VIS,
                                    KiwiLabel(113, 112, 2, 1650, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_40, CameraType.VIS,
                                    KiwiLabel(113, 112, 2, 1650, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_52, CameraType.VIS,
                                    KiwiLabel(106, 106, 2, 1400, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_52, CameraType.VIS,
                                    KiwiLabel(106, 106, 2, 1400, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_61, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_61, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_65, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_65, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_70, CameraType.VIS,
                                    KiwiLabel(111, 111, 2, 1850, 14.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_70, CameraType.VIS,
                                    KiwiLabel(111, 111, 2, 1850, 14.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_72, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_72, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_74, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_74, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_77, CameraType.VIS,
                                    KiwiLabel(128, 127, 2, 1700, 14, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_77, CameraType.VIS,
                                    KiwiLabel(128, 127, 2, 1700, 14, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_81, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_81, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_86, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_86, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_3, ID.ID_87, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_87, CameraType.VIS)]

day_m2_04_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_32, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_32, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_35, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_35, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_36, CameraType.VIS,
                                    AvocadoLabel(204, 197, 3, 0, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_36, CameraType.VIS,
                                    AvocadoLabel(204, 197, 3, 0, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_40, CameraType.VIS,
                                    AvocadoLabel(207, 200, 3, 550, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_40, CameraType.VIS,
                                    AvocadoLabel(207, 200, 3, 550, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_43, CameraType.VIS,
                                    AvocadoLabel(212, 204, 3, 600, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_43, CameraType.VIS,
                                    AvocadoLabel(212, 204, 3, 600, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_60, CameraType.VIS,
                                    AvocadoLabel(236, 228, 3, 750, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_60, CameraType.VIS,
                                    AvocadoLabel(236, 228, 3, 750, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_51, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_61, CameraType.VIS,
                                    KiwiLabel(130, 128, 3, 2150, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_61, CameraType.VIS,
                                    KiwiLabel(130, 128, 3, 2150, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_65, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_65, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_72, CameraType.VIS,
                                    KiwiLabel(127, 125, 3, 1900, 15, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_72, CameraType.VIS,
                                    KiwiLabel(127, 125, 3, 1900, 15, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_74, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_74, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
                        ## seems OVERRIPE
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, None, 3, None, None, RipenessState.OVERRIPE, "Damaged")),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_81, CameraType.VIS,
                                    KiwiLabel(122, 122, 3, 700, 15.5, RipenessState.PERFECT)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_81, CameraType.VIS,
                                    KiwiLabel(122, 122, 3, 700, 15.5, RipenessState.PERFECT)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_86, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_86, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_4, ID.ID_87, CameraType.VIS,
                                    KiwiLabel(119, 118, 3, 1625, 17.5, RipenessState.RIPE, "very sweet")),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_87, CameraType.VIS,
                                    KiwiLabel(119, 118, 3, 1625, 17.5, RipenessState.RIPE, "very sweet"))]

day_m2_05_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_32, CameraType.VIS,
                                    AvocadoLabel(211, 204, 4, 0, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_32, CameraType.VIS,
                                    AvocadoLabel(211, 204, 4, 0, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_35, CameraType.VIS,
                                    AvocadoLabel(216, 206, 4, 1250, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_35, CameraType.VIS,
                                    AvocadoLabel(216, 206, 4, 1250, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_41, CameraType.VIS,
                                    AvocadoLabel(209, 199, 4, 700, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_41, CameraType.VIS,
                                    AvocadoLabel(209, 199, 4, 700, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_5, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_5, ID.ID_58, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_51, CameraType.VIS,
                                    KiwiLabel(106, 105, 4, 1625, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_51, CameraType.VIS,
                                    KiwiLabel(106, 105, 4, 1625, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_65, CameraType.VIS,
                                    KiwiLabel(110, 108, 4, 600, 14.5, RipenessState.PERFECT)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_65, CameraType.VIS,
                                    KiwiLabel(110, 108, 4, 600, 14.5, RipenessState.PERFECT)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_74, CameraType.VIS,
                                    KiwiLabel(129, 128, 4, 2450, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_74, CameraType.VIS,
                                    KiwiLabel(129, 128, 4, 2450, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, 109, 4, 0, 14.5, RipenessState.OVERRIPE, "Damaged")),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_75, CameraType.VIS,
                                    KiwiLabel(111, 109, 4, 0, 14.5, RipenessState.OVERRIPE, "Damaged")),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_78, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_79, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_84, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_86, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_5, ID.ID_86, CameraType.VIS)]

day_m2_06_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_38, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_46, CameraType.VIS,
                                    AvocadoLabel(205, 194, 5, 0, RipenessState.OVERRIPE, "more than one day damaged!")),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_46, CameraType.VIS,
                                    AvocadoLabel(205, 194, 5, 0, RipenessState.OVERRIPE, "more than one day damaged!")),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_54, CameraType.VIS,
                                    AvocadoLabel(199, 185, 5, 0, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_54, CameraType.VIS,
                                    AvocadoLabel(199, 185, 5, 0, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_55, CameraType.VIS,
                                    AvocadoLabel(267, 255, 5, 700, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_55, CameraType.VIS,
                                    AvocadoLabel(267, 255, 5, 700, RipenessState.RIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_6, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_58, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_56, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_60, CameraType.VIS, ),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_60, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_78, CameraType.VIS,
                                    KiwiLabel(130, 128, 5, 1500, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_78, CameraType.VIS,
                                    KiwiLabel(130, 128, 5, 1500, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_79, CameraType.VIS,
                                    KiwiLabel(90, 88, 5, 1200, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_79, CameraType.VIS,
                                    KiwiLabel(90, 88, 5, 1200, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_83, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_84, CameraType.VIS,
                                    KiwiLabel(100, 98, 5, 1650, 15.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_84, CameraType.VIS,
                                    KiwiLabel(100, 98, 5, 1650, 15.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_6, ID.ID_86, CameraType.VIS,
                                    KiwiLabel(113, 113, 5, 1450, 15.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_6, ID.ID_86, CameraType.VIS,
                                    KiwiLabel(113, 113, 5, 1450, 15.5, RipenessState.RIPE))]

day_m2_07_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_38, CameraType.VIS,
                                    AvocadoLabel(232, 210, 7, 500, RipenessState.NEAR_OVERRIPE, "damaged")),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_38, CameraType.VIS,
                                    AvocadoLabel(232, 210, 7, 500, RipenessState.NEAR_OVERRIPE, "damaged")),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_45, CameraType.VIS,
                                    AvocadoLabel(246, 222, 7, 750, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_45, CameraType.VIS,
                                    AvocadoLabel(246, 222, 7, 750, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_7, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_58, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_49, CameraType.VIS,
                                    KiwiLabel(110, 107, 7, 1725, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_49, CameraType.VIS,
                                    KiwiLabel(110, 107, 7, 1725, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_54, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_56, CameraType.VIS,
                                    KiwiLabel(111, 109, 7, 1400, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_56, CameraType.VIS,
                                    KiwiLabel(111, 109, 7, 1400, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_60, CameraType.VIS,
                                    KiwiLabel(123, 119, 7, 1300, 16, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_60, CameraType.VIS,
                                    KiwiLabel(123, 119, 7, 1300, 16, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_63, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_82, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_7, ID.ID_83, CameraType.VIS,
                                    KiwiLabel(126, 121, 7, 3050, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_83, CameraType.VIS,
                                    KiwiLabel(126, 121, 7, 3050, 14, RipenessState.UNRIPE))]

day_m2_08_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_34, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_57, CameraType.VIS,
                                    AvocadoLabel(259, 229, 8, 800, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_57, CameraType.VIS,
                                    AvocadoLabel(259, 229, 8, 800, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_8, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_8, ID.ID_58, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_47, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_54, CameraType.VIS,
                                    KiwiLabel(111, 108, 8, 1825, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_54, CameraType.VIS,
                                    KiwiLabel(111, 108, 8, 1825, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_59, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_63, CameraType.VIS,
                                    KiwiLabel(106, 102, 8, 775, 13.5, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_63, CameraType.VIS,
                                    KiwiLabel(106, 102, 8, 775, 13.5, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_80, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_82, CameraType.VIS,
                                    KiwiLabel(107, 103, 8, 1950, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_82, CameraType.VIS,
                                    KiwiLabel(107, 103, 8, 1950, 15, RipenessState.RIPE))]

day_m2_09_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_34, CameraType.VIS,
                                    AvocadoLabel(201, 171, 9, 0, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_34, CameraType.VIS,
                                    AvocadoLabel(201, 171, 9, 0, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_37, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_48, CameraType.VIS,
                                    AvocadoLabel(239, 211, 9, 1050, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_48, CameraType.VIS,
                                    AvocadoLabel(239, 211, 9, 1050, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_49, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_58, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_46, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_47, CameraType.VIS,
                                    KiwiLabel(108, 105, 9, 1425, 13.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_47, CameraType.VIS,
                                    KiwiLabel(108, 105, 9, 1425, 13.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_55, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_59, CameraType.VIS,
                                    KiwiLabel(105, 103, 9, 1800, 14.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_59, CameraType.VIS,
                                    KiwiLabel(105, 103, 9, 1800, 14.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_9, ID.ID_80, CameraType.VIS,
                                    KiwiLabel(124, 120, 9, 3000, 15.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_9, ID.ID_80, CameraType.VIS,
                                    KiwiLabel(124, 120, 9, 3000, 15.5, RipenessState.UNRIPE))]

day_m2_10_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_10, ID.ID_37, CameraType.VIS,
                                    AvocadoLabel(199, 154, 10, 0, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_10, ID.ID_37, CameraType.VIS,
                                    AvocadoLabel(199, 154, 10, 0, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_10, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_10, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_10, ID.ID_44, CameraType.VIS,
                                    AvocadoLabel(200, 157, 10, 0, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_10, ID.ID_44, CameraType.VIS,
                                    AvocadoLabel(200, 157, 10, 0, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_10, ID.ID_49, CameraType.VIS,
                                    AvocadoLabel(211, 182, 10, 550, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_10, ID.ID_49, CameraType.VIS,
                                    AvocadoLabel(211, 182, 10, 550, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_10, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_10, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_10, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_10, ID.ID_58, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_46, CameraType.VIS,
                                    KiwiLabel(105, 102, 10, 2200, 12.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_46, CameraType.VIS,
                                    KiwiLabel(105, 102, 10, 2200, 12.5, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_55, CameraType.VIS,
                                    KiwiLabel(111, 108, 10, 1800, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_55, CameraType.VIS,
                                    KiwiLabel(111, 108, 10, 1800, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_58, CameraType.VIS,
                                    KiwiLabel(107, 102, 10, 1650, 15.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_58, CameraType.VIS,
                                    KiwiLabel(107, 102, 10, 1650, 15.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_66, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_68, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_73, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_76, CameraType.VIS)]

day_m2_11_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_11, ID.ID_42, CameraType.VIS,
                                    AvocadoLabel(225, 198, 11, 700, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_11, ID.ID_42, CameraType.VIS,
                                    AvocadoLabel(225, 198, 11, 700, RipenessState.PERFECT)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_11, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_11, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_11, ID.ID_58, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_11, ID.ID_58, CameraType.VIS),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_66, CameraType.VIS,
                                    KiwiLabel(91, 87, 11, 1250, 17.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_66, CameraType.VIS,
                                    KiwiLabel(91, 87, 11, 1250, 17.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_68, CameraType.VIS,
                                    KiwiLabel(100, 95, 11, 600, 15, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_68, CameraType.VIS,
                                    KiwiLabel(100, 95, 11, 600, 15, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_73, CameraType.VIS,
                                    KiwiLabel(122, 117, 11, 1900, 16, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_73, CameraType.VIS,
                                    KiwiLabel(122, 117, 11, 1900, 16, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_11, ID.ID_76, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_76, CameraType.VIS)]

day_m2_12_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_12, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_12, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_12, ID.ID_58, CameraType.VIS,
                                    AvocadoLabel(234, None, 12, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_12, ID.ID_58, CameraType.VIS,
                                    AvocadoLabel(234, None, 12, None, RipenessState.OVERRIPE)),

                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_42, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_64, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_12, ID.ID_76, CameraType.VIS,
                                    KiwiLabel(123, 117, 12, 2300, 15, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_76, CameraType.VIS,
                                    KiwiLabel(123, 117, 12, 2300, 15, RipenessState.UNRIPE))]

day_m2_13_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_13, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_13, ID.ID_53, CameraType.VIS),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_13, ID.ID_58, CameraType.VIS,
                                    AvocadoLabel(234, None, 14, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_13, ID.ID_58, CameraType.VIS,
                                    AvocadoLabel(234, None, 14, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_41, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_42, CameraType.VIS,
                                    KiwiLabel(105, 100, 14, 1700, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_42, CameraType.VIS,
                                    KiwiLabel(105, 100, 14, 1700, 14.5, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_48, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_64, CameraType.VIS,
                                    KiwiLabel(125, 116, 14, 2100, 16, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_64, CameraType.VIS,
                                    KiwiLabel(125, 116, 14, 2100, 16, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_67, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_13, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_13, ID.ID_69, CameraType.VIS)]

day_m2_14_all_fruits = [FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_14, ID.ID_53, CameraType.VIS,
                                    AvocadoLabel(259, 224, 15, 1000, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_14, ID.ID_53, CameraType.VIS,
                                    AvocadoLabel(259, 224, 15, 1000, RipenessState.NEAR_OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_14, ID.ID_58, CameraType.VIS,
                                    AvocadoLabel(234, 194, 15, 0, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_14, ID.ID_58, CameraType.VIS,
                                    AvocadoLabel(234, 194, 15, 0, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_41, CameraType.VIS,
                                    KiwiLabel(105, 100, 15, 1800, 13, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_41, CameraType.VIS,
                                    KiwiLabel(105, 100, 15, 1800, 13, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_45, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, None, 15, None, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, None, 15, None, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_67, CameraType.VIS,
                                    KiwiLabel(125, 118, 15, 2150, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_67, CameraType.VIS,
                                    KiwiLabel(125, 118, 15, 2150, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_69, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_14, ID.ID_69, CameraType.VIS)]

day_m2_15_all_fruits = [FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_45, CameraType.VIS,
                                    KiwiLabel(115, 108, 16, 500, 13, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_45, CameraType.VIS,
                                    KiwiLabel(115, 108, 16, 500, 13, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, None, 16, None, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, None, 16, None, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_50, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_57, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_69, CameraType.VIS,
                                    KiwiLabel(125, 117, 16, 3200, 15, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_69, CameraType.VIS,
                                    KiwiLabel(125, 117, 16, 3200, 15, RipenessState.UNRIPE))]

day_m2_16_all_fruits = [FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_16, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_16, ID.ID_44, CameraType.VIS),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_16, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, None, 17, None, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_16, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, None, 17, None, None, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_16, ID.ID_50, CameraType.VIS,
                                    KiwiLabel(117, 109, 17, 1750, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_16, ID.ID_50, CameraType.VIS,
                                    KiwiLabel(117, 109, 17, 1750, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_16, ID.ID_57, CameraType.VIS,
                                    KiwiLabel(111, 103, 17, 2450, 15, RipenessState.RIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_16, ID.ID_57, CameraType.VIS,
                                    KiwiLabel(111, 103, 17, 2450, 15, RipenessState.RIPE))]

day_m2_17_all_fruits = [FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_17, ID.ID_44, CameraType.VIS,
                                    KiwiLabel(106, 98, 18, 2400, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_17, ID.ID_44, CameraType.VIS,
                                    KiwiLabel(106, 98, 18, 2400, 14, RipenessState.UNRIPE)),
                        FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_17, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, 104, 18, 0, 15, RipenessState.OVERRIPE)),
                        FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_17, ID.ID_48, CameraType.VIS,
                                    KiwiLabel(113, 104, 18, 0, 15, RipenessState.OVERRIPE))]

test_set_fruits = [FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_3, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_3, ID.ID_52, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_33, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_3, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_23, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_4, ID.ID_43, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_25, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_6, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_7, ID.ID_45, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_2, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_10, ID.ID_44, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_22, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_9, ID.ID_22, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_6, ID.ID_46, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_7, CameraType.VIS),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_3, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_13, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_3, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_5, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_7, ID.ID_27, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_19, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_8, ID.ID_10, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_28, CameraType.NIR),
                   FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_7, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_12, ID.ID_76, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_51, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_26, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_32, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_18, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_10, ID.ID_55, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_10, ID.ID_46, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_71, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_73, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_36, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_16, ID.ID_57, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_29, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_11, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_5, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_16, ID.ID_50, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_23, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_13, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_16, ID.ID_48, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_11, ID.ID_68, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_45, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_63, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_13, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_20, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_16, CameraType.VIS),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_7, ID.ID_24, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_26, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_32, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_8, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_2, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_12, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_7, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_10, ID.ID_27, CameraType.NIR),
                   FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_10, ID.ID_27, CameraType.NIR)]

val_set_fruits = [FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_13, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_13, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_47, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_3, ID.ID_52, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_5, ID.ID_23, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_4, ID.ID_43, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_2, ID.ID_50, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_48, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_18, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_4, ID.ID_16, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_13, ID.ID_58, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_10, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_9, ID.ID_34, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_M2_9, ID.ID_34, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_M2_14, ID.ID_53, CameraType.VIS),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_3, ID.ID_17, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_3, ID.ID_17, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_5, ID.ID_23, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_6, ID.ID_25, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_7, ID.ID_27, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.BACK, Day.DAY_6, ID.ID_19, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_8, ID.ID_10, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_9, ID.ID_29, CameraType.NIR),
                  FruitRecord(Fruit.AVOCADO, Side.FRONT, Day.DAY_10, ID.ID_24, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_5, ID.ID_26, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_8, ID.ID_54, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_69, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_5, ID.ID_74, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_39, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_24, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_14, ID.ID_41, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_3, ID.ID_19, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_16, ID.ID_50, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_3, ID.ID_17, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_38, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_60, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_12, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_7, ID.ID_49, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_4, ID.ID_87, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_3, ID.ID_52, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_22, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_62, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_75, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_1, ID.ID_62, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_15, ID.ID_48, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_M2_15, ID.ID_45, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_1, ID.ID_75, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_17, ID.ID_48, CameraType.VIS),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_4, ID.ID_18, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_26, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_5, ID.ID_32, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_35, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_6, ID.ID_11, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_6, ID.ID_1, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_7, ID.ID_16, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_4, ID.ID_13, CameraType.NIR),
                  FruitRecord(Fruit.KIWI, Side.BACK, Day.DAY_8, ID.ID_4, CameraType.NIR)]


def get_dataset(r: FruitRecord):
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


temperature_M2 = [
    (Day.DAY_M2_1, 20.),
    (Day.DAY_M2_2, 20.),
    (Day.DAY_M2_3, 20.),
    (Day.DAY_M2_4, 21.),
    (Day.DAY_M2_5, 20.),
    (Day.DAY_M2_6, 20.),
    (Day.DAY_M2_7, 20.),
    (Day.DAY_M2_8, 19.5),
    (Day.DAY_M2_9, 20),
    (Day.DAY_M2_10, 20),
    (Day.DAY_M2_11, 20),
    (Day.DAY_M2_12, 20),
    (Day.DAY_M2_13, 20),
    (Day.DAY_M2_14, 20.5),
    (Day.DAY_M2_15, 21),
    (Day.DAY_M2_16, 21.5),
    (Day.DAY_M2_17, 21.5)
]

all_fruits_m1 = np.concatenate((day_1_all_fruits, day_2_all_fruits, day_3_all_fruits,
                                day_4_all_fruits, day_5_all_fruits, day_6_all_fruits, day_7_all_fruits,
                                day_8_all_fruits, day_9_all_fruits, day_10_all_fruits, day_11_all_fruits))

# Here the first and the second day are removed
# The second day has some artefacts in the lower bands, probably bad referencing
all_fruits_m1_better = np.concatenate((day_3_all_fruits,
                                       day_4_all_fruits, day_5_all_fruits, day_6_all_fruits, day_7_all_fruits,
                                       day_8_all_fruits, day_9_all_fruits, day_10_all_fruits))

# The measurements of day 11 are broken. Maybe the references are incorrect
all_fruits_m1_cleaned = np.concatenate((day_1_all_fruits, day_2_all_fruits, day_3_all_fruits,
                                        day_4_all_fruits, day_5_all_fruits, day_6_all_fruits, day_7_all_fruits,
                                        day_8_all_fruits, day_9_all_fruits, day_10_all_fruits))

all_fruits_m2 = np.concatenate((day_m2_01_all_fruits, day_m2_02_all_fruits, day_m2_03_all_fruits, day_m2_04_all_fruits,
                                day_m2_05_all_fruits, day_m2_06_all_fruits, day_m2_07_all_fruits, day_m2_08_all_fruits,
                                day_m2_09_all_fruits, day_m2_10_all_fruits, day_m2_11_all_fruits, day_m2_12_all_fruits,
                                day_m2_13_all_fruits, day_m2_14_all_fruits, day_m2_15_all_fruits, day_m2_16_all_fruits,
                                day_m2_17_all_fruits))

all_fruits = np.concatenate((all_fruits_m1_cleaned, all_fruits_m2))


# ///


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
            {'id': 'NIR', 'name': 'INNOSPEC RedEye', 'wavelengths': util.get_wavelengths_for(CameraType.NIR)}
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

        if isinstance(r.label, KiwiLabel):
            a_j['sugar_content']: r.label.sugar_content

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

    rest, test = extract_test_data(all_fruits)
    train, val = extract_val_data(rest)
    json.dump(to_json(test), open("../dataset/test.json", "w"))
    json.dump(to_json(val), open("../dataset/val.json", "w"))
    json.dump(to_json(get_labeled_fruits(train)), open("../dataset/train_only_labeled.json", "w"))
    json.dump(to_json(train), open("../dataset/train_all.json", "w"))
