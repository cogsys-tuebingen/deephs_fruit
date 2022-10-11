from core.name_convention import *
import numpy as np

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