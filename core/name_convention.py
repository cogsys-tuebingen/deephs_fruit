import os
import enum
from typing import Union

import core.spectral_io as spectral_io


class Side(enum.Enum):
    FRONT = 'front'
    BACK = 'back'


class Day(enum.Enum):
    TEST_1 = 'test'
    TEST_2 = 'test2'
    DAY_1 = 'day_01'
    DAY_2 = 'day_02'
    DAY_3 = 'day_03'
    DAY_4 = 'day_04'
    DAY_5 = 'day_05'
    DAY_6 = 'day_06'
    DAY_7 = 'day_07'
    DAY_8 = 'day_08'
    DAY_9 = 'day_09'
    DAY_10 = 'day_10'
    DAY_11 = 'day_11'
    DAY_M2_1 = 'day_m2_01'
    DAY_M2_2 = 'day_m2_02'
    DAY_M2_3 = 'day_m2_03'
    DAY_M2_4 = 'day_m2_04'
    DAY_M2_5 = 'day_m2_05'
    DAY_M2_6 = 'day_m2_06'
    DAY_M2_7 = 'day_m2_07'
    DAY_M2_8 = 'day_m2_08'
    DAY_M2_9 = 'day_m2_09'
    DAY_M2_10 = 'day_m2_10'
    DAY_M2_11 = 'day_m2_11'
    DAY_M2_12 = 'day_m2_12'
    DAY_M2_13 = 'day_m2_13'
    DAY_M2_14 = 'day_m2_14'
    DAY_M2_15 = 'day_m2_15'
    DAY_M2_16 = 'day_m2_16'
    DAY_M2_17 = 'day_m2_17'


class CameraType(enum.Enum):
    VIS = 'VIS'
    NIR = 'NIR'
    RGB = 'RGB'


class Fruit(enum.Enum):
    AVOCADO = 'Avocado'
    KIWI = 'Kiwi'


class ID(enum.Enum):
    UNKNOWN = '?'
    ID_1 = '01'
    ID_2 = '02'
    ID_3 = '03'
    ID_4 = '04'
    ID_5 = '05'
    ID_6 = '06'
    ID_7 = '07'
    ID_8 = '08'
    ID_9 = '09'
    ID_10 = '10'
    ID_11 = '11'
    ID_12 = '12'
    ID_13 = '13'
    ID_14 = '14'
    ID_15 = '15'
    ID_16 = '16'
    ID_17 = '17'
    ID_18 = '18'
    ID_19 = '19'
    ID_20 = '20'
    ID_21 = '21'
    ID_22 = '22'
    ID_23 = '23'
    ID_24 = '24'
    ID_25 = '25'
    ID_26 = '26'
    ID_27 = '27'
    ID_28 = '28'
    ID_29 = '29'
    ID_30 = '30'
    ID_31 = '31'
    ID_32 = '32'
    ID_33 = '33'
    ID_34 = '34'
    ID_35 = '35'
    ID_36 = '36'
    ID_37 = '37'
    ID_38 = '38'
    ID_39 = '39'
    ID_40 = '40'
    ID_41 = '41'
    ID_42 = '42'
    ID_43 = '43'
    ID_44 = '44'
    ID_45 = '45'
    ID_46 = '46'
    ID_47 = '47'
    ID_48 = '48'
    ID_49 = '49'
    ID_50 = '50'
    ID_51 = '51'
    ID_52 = '52'
    ID_53 = '53'
    ID_54 = '54'
    ID_55 = '55'
    ID_56 = '56'
    ID_57 = '57'
    ID_58 = '58'
    ID_59 = '59'
    ID_60 = '60'
    ID_61 = '61'
    ID_62 = '62'
    ID_63 = '63'
    ID_64 = '64'
    ID_65 = '65'
    ID_66 = '66'
    ID_67 = '67'
    ID_68 = '68'
    ID_69 = '69'
    ID_70 = '70'
    ID_71 = '71'
    ID_72 = '72'
    ID_73 = '73'
    ID_74 = '74'
    ID_75 = '75'
    ID_76 = '76'
    ID_77 = '77'
    ID_78 = '78'
    ID_79 = '79'
    ID_80 = '80'
    ID_81 = '81'
    ID_82 = '82'
    ID_83 = '83'
    ID_84 = '84'
    ID_85 = '85'
    ID_86 = '86'
    ID_87 = '87'
    ID_88 = '88'
    ID_89 = '89'
    ID_90 = '90'
    ID_91 = '91'
    ID_92 = '92'
    ID_93 = '93'
    ID_94 = '94'
    ID_95 = '95'
    ID_96 = '96'
    ID_97 = '97'
    ID_98 = '98'
    ID_99 = '99'


class DATASET_TYPE(enum.Enum):
    TRAIN = "train",
    VAL = "validation",
    TEST = "test"



def get_file_path(fruit: Fruit, side: Side, day: Day, id: ID, camera_type: CameraType):
    name = get_name(fruit, id, side, day)
    file_name = os.path.join(fruit.value.capitalize(), camera_type.value.upper(), day.value.lower(), name)

    return file_name


def get_name(fruit: Fruit, id:ID, side: Side, day: Day):
    if day == Day.TEST_1 or day == Day.TEST_2:
        name = fruit.value.lower() + "_" + day.value.lower() + "_" + side.value.lower()
    else:
        name = fruit.value.lower() + "_" + day.value.lower() + "_" + id.value + "_" + side.value.lower()
    return name


def get_unique_name(fruit: Fruit, id:ID, side: Side, day: Day, camera_type:CameraType, postfix: str = None):

    if postfix is None:
        name = fruit.value.lower() + "_" + day.value.lower() + "_" + id.value +\
               "_" + side.value.lower() + "_" + camera_type.value.lower()
    else:
        name = fruit.value.lower() + "_" + day.value.lower() + "_" + id.value +\
               "_" + side.value.lower() + "_" + camera_type.value.lower() + "_" + postfix
    return name


class RipenessState(enum.Enum):
    UNRIPE = 'unripe'
    RIPE = 'ripe'
    PERFECT = 'perfect'  # necessary?
    NEAR_OVERRIPE = 'near_overripe'  # necessary?
    OVERRIPE = 'overripe'


def ripeness2int(_ripeness_state: RipenessState):
    if _ripeness_state == RipenessState.UNRIPE:
        return 0
    if _ripeness_state == RipenessState.RIPE:
        return 3
    if _ripeness_state == RipenessState.PERFECT:
        return 1
    if _ripeness_state == RipenessState.NEAR_OVERRIPE:
        return 4
    if _ripeness_state == RipenessState.OVERRIPE:
        return 2


def int2ripeness(_ripeness_int: int):
    if _ripeness_int == 0:
        return RipenessState.UNRIPE
    if _ripeness_int == 3:
        return RipenessState.RIPE
    if _ripeness_int == 1:
        return RipenessState.PERFECT
    if _ripeness_int == 4:
        return RipenessState.NEAR_OVERRIPE
    if _ripeness_int == 2:
        return RipenessState.OVERRIPE


def ripeness2color(_ripeness: RipenessState):
    if _ripeness == RipenessState.UNRIPE:
        return 'g'
    if _ripeness == RipenessState.RIPE or _ripeness == RipenessState.PERFECT:
        return 'y'
    if _ripeness == RipenessState.OVERRIPE:
        return 'r'
    
    return 'b'


class FirmnessLevel(enum.Enum):
    TOO_HARD = 'too_hard'
    READY = 'ready'
    TOO_SOFT = 'too_soft'


def firmness2int(_ripeness_state: FirmnessLevel):
    if _ripeness_state == FirmnessLevel.TOO_HARD:
        return 0
    if _ripeness_state == FirmnessLevel.READY:
        return 1
    if _ripeness_state == FirmnessLevel.TOO_SOFT:
        return 2


def int2firmness(_i: int):
    if _i == 0:
        return FirmnessLevel.TOO_HARD
    if _i == 1:
        return FirmnessLevel.READY
    if _i == 2:
        return FirmnessLevel.TOO_SOFT


def firmness2color(_ripeness: FirmnessLevel):
    if _ripeness == FirmnessLevel.TOO_HARD:
        return 'g'
    if _ripeness == FirmnessLevel.READY:
        return 'y'
    if _ripeness == FirmnessLevel.TOO_SOFT:
        return 'r'

    return 'b'


class SugarLevel(enum.Enum):
    NOT_SWEET = 'not_sweet'
    READY = 'ready'
    TOO_SWEET = 'too_sweet'


def sugar2int(_ripeness_state: SugarLevel):
    if _ripeness_state == SugarLevel.NOT_SWEET:
        return 0
    if _ripeness_state == SugarLevel.READY:
        return 1
    if _ripeness_state == SugarLevel.TOO_SWEET:
        return 2


def int2sugar(_i: int):
    if _i == 0:
        return SugarLevel.NOT_SWEET
    if _i == 1:
        return SugarLevel.READY
    if _i == 2:
        return SugarLevel.TOO_SWEET


def sugar2color(_ripeness: SugarLevel):
    if _ripeness == SugarLevel.NOT_SWEET:
        return 'g'
    if _ripeness == SugarLevel.READY:
        return 'y'
    if _ripeness == SugarLevel.TOO_SWEET:
        return 'r'

    return 'b'


class AvocadoLabel:
    def __init__(self, _init_weight: int, _end_weight: int, _storage_days: int, _firmness: int,
                 _ripeness_state: RipenessState, _comment: str = None):
        self.init_weight = _init_weight
        self.end_weight = _end_weight
        self.storage_days = _storage_days
        self.firmness = _firmness  # in g / cm^2
        self.ripeness_state = _ripeness_state
        self.comment = _comment

    def __str__(self):
        if self.comment is not None:
            return "{%s, firmness: %s, comment: '%s'}" % (
                self.ripeness_state.value, self.firmness, self.comment)
        else:
            return "{%s, firmness: %s}" % (
                self.ripeness_state.value, self.firmness)

    def get_firmness_level(self) -> FirmnessLevel:
        if self.firmness > 1200:
            return FirmnessLevel.TOO_HARD
        elif self.firmness < 900:
            return FirmnessLevel.TOO_SOFT
        else:
            return FirmnessLevel.READY


class KiwiLabel:
    def __init__(self, _init_weight: int, _end_weight: int, _storage_days: int, _firmness: int, _sugar_content: float,
                 _ripeness_state: RipenessState, _comment: str = None):
        self.init_weight = _init_weight
        self.end_weight = _end_weight
        self.storage_days = _storage_days
        self.firmness = _firmness  # in g / cm^2
        self.sugar_content = _sugar_content  # in °Brix
        self.ripeness_state = _ripeness_state
        self.comment = _comment

    def __str__(self):
        if self.comment is not None:
            return "{%s, firmness: %s, sugar content: %s, comment: '%s'}" % (
                self.ripeness_state.value, self.firmness, self.sugar_content, self.comment)
        else:
            return "{%s, firmness: %s, sugar content: %s}" % (
                self.ripeness_state.value, self.firmness, self.sugar_content)

    def get_firmness_level(self) -> FirmnessLevel:
        if self.firmness > 1500:
            return FirmnessLevel.TOO_HARD
        elif self.firmness < 1000:
            return FirmnessLevel.TOO_SOFT
        else:
            return FirmnessLevel.READY

    def get_sugar_level(self) -> SugarLevel:
        if self.sugar_content < 15.5:
            return SugarLevel.NOT_SWEET
        elif self.sugar_content > 17:
            return SugarLevel.TOO_SWEET
        else:
            return SugarLevel.READY


import core.util as util

class FruitRecord:
    def __init__(self, fruit: Fruit, side: Side, day: Day, id: ID, camera_type: CameraType,
                 label: Union[AvocadoLabel, KiwiLabel] = None):
        self.fruit = fruit
        self.id = id
        self.side = side
        self.day = day
        self.camera_type = camera_type
        self.label = label

    def get_file_path(self):
        return get_file_path(self.fruit, self.side, self.day,  self.id, self.camera_type)

    def get_name(self):
        return get_name(self.fruit, self.id, self.side, self.day)

    def get_unique_name(self, _postfix: str = None):
        return get_unique_name(self.fruit, self.id, self.side, self.day, self.camera_type, _postfix)

    def load(self, _origin=None, is_already_referenced=False):
        # print("# Load cube: %s " % self.get_unique_name())

        if self.camera_type in (CameraType.VIS, CameraType.NIR):
            if is_already_referenced:
                header, data = spectral_io.load_envi(self.get_file_path(), _origin)
            else:
                header, data = spectral_io.load_referenced_envi(self.get_file_path(), _origin)

            return header, data

    def is_labeled(self):
        return self.label is not None

    def __str__(self):
        if self.is_labeled():
            return "{%s : %s/%s \n" \
                   "\ton day: %s\n" \
                   "\trecored with: %s\n" \
                   "\thas state: %s}" % (self.fruit.value, self.id.value, self.side.value,
                                            self.day.value, self.camera_type.value, self.label)
        else:
            return "{%s : %s/%s \n" \
                "\ton day: %s\n" \
                "\trecored with: %s}" % (self.fruit.value, self.id.value, self.side.value,
                                         self.day.value, self.camera_type.value)

    def __eq__(self, other: Fruit):
        if not isinstance(other, FruitRecord):
            return False

        return (self.fruit == other.fruit) and (self.camera_type == other.camera_type) and (self.side == other.side) and \
               (self.id == other.id) and (self.day == other.day)

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))


class ClassificationType(enum.Enum):
    RIPENESS = 'ripeness'
    FIRMNESS = 'firmness'
    SUGAR = 'sugar'


def label2text(l, _english=False):
    if not _english:
        if l == RipenessState.UNRIPE:
            return 'Unreif'
        if l == RipenessState.RIPE:
            return 'Reif'
        if l == RipenessState.PERFECT:
            return 'Perfekt'
        if l == RipenessState.OVERRIPE:
            return 'Überreif'
        if l == RipenessState.NEAR_OVERRIPE:
            return 'Nahe überreif'
        if l == FirmnessLevel.TOO_HARD:
            return 'Zu hart'
        if l == FirmnessLevel.READY:
            return 'Gut'
        if l == FirmnessLevel.TOO_SOFT:
            return 'Zu weich'
        if l == SugarLevel.NOT_SWEET:
            return 'Nicht süß'
        if l == SugarLevel.READY:
            return 'Gut'
        if l == SugarLevel.TOO_SWEET:
            return 'Zu süß'
    else:
        if l == RipenessState.UNRIPE:
            return 'Unripe'
        if l == RipenessState.RIPE:
            return 'Ripe'
        if l == RipenessState.PERFECT:
            return 'Ready'
        if l == RipenessState.OVERRIPE:
            return 'Overripe'
        if l == RipenessState.NEAR_OVERRIPE:
            return 'Near overripe'
        if l == FirmnessLevel.TOO_HARD:
            return 'Too hard'
        if l == FirmnessLevel.READY:
            return 'Ready'
        if l == FirmnessLevel.TOO_SOFT:
            return 'Too soft'
        if l == SugarLevel.NOT_SWEET:
            return 'Not sweet'
        if l == SugarLevel.READY:
            return 'Ready'
        if l == SugarLevel.TOO_SWEET:
            return 'Too sweet'



