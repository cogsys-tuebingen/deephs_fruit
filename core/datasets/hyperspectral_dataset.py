from torch.utils.data import Dataset
import torch

from core.name_convention import *
from core.measurements import *
import core.util as util
import core.fruit_list as fruit_list
import cv2
import numpy as np
import copy


class HyperspectralDataset(Dataset):
    def __init__(self, classification_type, records, data_path, balance=False, transform=None, input_size=(62, 62)):
        assert len(records) > 0

        self.classification_type = classification_type
        self._org_records = records
        self.records = self._org_records
        self.data_path = data_path
        self.balance = balance
        self.input_size = input_size

        self.transform = transform

        self._preload_data()

        if self.balance:
            self.records = self._org_records.copy()
            self._balance_classes()

    def __len__(self):
        return len(self.records)

    def _preload_data(self):
        print("# Preload data")
        self.fruit_data = {}
        for r in self.records:
            self.fruit_data[r] = prepare_fruit(
                r, self.data_path, input_size=self.input_size)
        print("# done.")

    def _balance_classes(self):
        if self.classification_type == ClassificationType.RIPENESS:
            states = [RipenessState.UNRIPE, RipenessState.RIPE, RipenessState.PERFECT, RipenessState.NEAR_OVERRIPE,
                      RipenessState.OVERRIPE]
        if self.classification_type == ClassificationType.FIRMNESS:
            states = [FirmnessLevel.TOO_SOFT,
                      FirmnessLevel.READY, FirmnessLevel.TOO_HARD]
        if self.classification_type == ClassificationType.SUGAR:
            states = [SugarLevel.NOT_SWEET,
                      SugarLevel.READY, SugarLevel.TOO_SWEET]

        def get_label(record):
            if self.classification_type == ClassificationType.RIPENESS:
                return record.label.ripeness_state
            if self.classification_type == ClassificationType.FIRMNESS:
                return record.label.get_firmness_level()
            if self.classification_type == ClassificationType.SUGAR:
                return record.label.get_sugar_level()

        max_count = 0
        for s in states:
            count = len([r for r in self.records if get_label(r) == s])
            print("%s #: %i" % (s, count))
            max_count = max(max_count, count)

        self.balance_to = max_count

        print("# Augment data to get balanced classes of size %i" %
              self.balance_to)

        target_class_size = self.balance_to
        # the sets are unbalanced, so augment the data to get balance sets
        for s in states:
            class_records = [r for r in self.records if get_label(r) == s]

            if len(class_records) == 0:
                continue

            print("# Augment: %s to %i elements" % (s, target_class_size))

            missing_objects_count = target_class_size - len(class_records)
            for i in range(missing_objects_count):
                new_record = class_records[np.random.randint(
                    0, len(class_records))]
                self.records = np.concatenate((self.records, [new_record]))

        print("# Data augmented")

        for s in states:
            count = len([r for r in self.records if get_label(r) == s])
            print("%s #: %i" % (s, count))

    def __getitem__(self, index):
        item = self.records[index]

        label = None

        if self.classification_type == ClassificationType.RIPENESS:
            label = torch.tensor(ripeness2int(item.label.ripeness_state))
        if self.classification_type == ClassificationType.FIRMNESS:
            label = torch.tensor(firmness2int(item.label.get_firmness_level()))
        if self.classification_type == ClassificationType.SUGAR:
            label = torch.tensor(sugar2int(item.label.get_sugar_level()))

        assert label is not None

        channel_wavelengths = torch.tensor(util.get_wavelengths_for(item.camera_type),
                                           requires_grad=False)

        item = torch.tensor(self.fruit_data[item])

        if self.transform is not None:
            item, label, channel_wavelengths = self.transform([item, label,
                                                               channel_wavelengths])

        return item, label, channel_wavelengths


def collater(batch):
    x = [b[0] for b in batch]
    y = [b[1] for b in batch]

    return x, y


def merge_ripeness_levels(records):
    """
        This function creates three classes out of the five label classes

        NEAR_OVERRIPE -> OVERRIPE
        RIPE -> PERFECT
    """

    for r in records:
        if r.label.ripeness_state == RipenessState.NEAR_OVERRIPE:
            r.label.ripeness_state = RipenessState.OVERRIPE
        elif r.label.ripeness_state == RipenessState.RIPE:
            r.label.ripeness_state = RipenessState.PERFECT

    return records


def extend_unripe_recordings(records):
    """
        All records previous to a unripe label are unripe too
    """

    # find unripe fruit
    unripe_fruit = [r for r in records if r.is_labeled()
                        and (r.label.ripeness_state in
                             [RipenessState.UNRIPE, RipenessState.RIPE])]
    unripe_fruit_ids = [r.id for r in unripe_fruit]

    unripe_label = copy.copy(unripe_fruit[0].label)
    unripe_label.comment = "Extended by time assumption"

    for r in records:
        if not r.is_labeled() and r.id in unripe_fruit_ids:
            r.label = unripe_label

    return records


def extend_too_firm_recordings(records: [FruitRecord]):
    """
        All records previous to a to_firm label are to_firm too
    """

    toofirm_fruit = [r for r in records if r.is_labeled() and r.label.firmness is not None
                        and (r.label.get_firmness_level()
                             in
                             [FirmnessLevel.TOO_HARD])]
    toofirm_fruit_ids = [r.id for r in toofirm_fruit]


    toofirm_label = copy.copy(toofirm_fruit[0].label)
    toofirm_label.comment = "Extended by time assumption"
    

    for r in records:
        if not r.is_labeled() and r.id in toofirm_fruit_ids:
            r.label = toofirm_label

    return records

def extend_too_unsweet_recordings(records: [FruitRecord]):
    """
        All records previous to a to_firm label are to_firm too
    """

    toounsweet_fruit = [r for r in records if r.is_labeled()
                        and r.label.sugar_content is not None and
                        (r.label.get_sugar_level() in [SugarLevel.NOT_SWEET])]
    toounsweet_fruit_ids = [r.id for r in toounsweet_fruit]


    toounsweet_label = copy.copy(toounsweet_fruit[0].label)
    toounsweet_label.comment = "Extended by time assumption"
    

    for r in records:
        if not r.is_labeled() and r.id in toounsweet_fruit_ids:
            r.label = toounsweet_label

    return records

def get_records(fruit, camera_type, classification_type,
                extend_by_time_assumption=False, use_inter_ripeness_levels=False, allow_all_fruit_types=False,
                use_new_recordings=False
               ):

    full_set = all_fruits_new if use_new_recordings else all_fruits

    if fruit == Fruit.ALL and not allow_all_fruit_types:
        raise NotImplementedError("ALL fruit types is not supported for this classifier!")

    records = fruit_list.get_for_camera_type(fruit_list.get_for_fruit(
        full_set, fruit), camera_type)

    assert len(records) > 0

    if extend_by_time_assumption:
        if classification_type == ClassificationType.RIPENESS:
            records = extend_unripe_recordings(records)
        elif classification_type == ClassificationType.FIRMNESS:
            records = extend_too_firm_recordings(records)
        elif classification_type == ClassificationType.SUGAR:
            records = extend_too_unsweet_recordings(records)

    records = fruit_list.get_labeled_fruits(records)

    if use_inter_ripeness_levels:
        records = merge_ripeness_levels(records)

    if classification_type == ClassificationType.RIPENESS:
        records = np.concatenate((fruit_list.get_fruits_with_state(records, RipenessState.UNRIPE),
                                  fruit_list.get_fruits_with_state(
                                      records, RipenessState.PERFECT),
                                  fruit_list.get_fruits_with_state(records, RipenessState.OVERRIPE)))
    if classification_type == ClassificationType.FIRMNESS:
        records = np.concatenate((fruit_list.get_fruits_with_firmness_level(records, FirmnessLevel.TOO_SOFT),
                                  fruit_list.get_fruits_with_firmness_level(
                                      records, FirmnessLevel.READY),
                                  fruit_list.get_fruits_with_firmness_level(records, FirmnessLevel.TOO_HARD)))
    if classification_type == ClassificationType.SUGAR:
        records = np.concatenate((fruit_list.get_fruits_with_sugar_level(records, SugarLevel.NOT_SWEET),
                                  fruit_list.get_fruits_with_sugar_level(
                                      records, SugarLevel.READY),
                                  fruit_list.get_fruits_with_sugar_level(records, SugarLevel.TOO_SWEET)))

    rest_records, test_records = fruit_list.extract_test_data(records)
    train_records, val_records = fruit_list.extract_val_data(rest_records)

    return train_records, val_records, test_records


def add_border(_obj):
    enlarged = np.zeros(
        (_obj.shape[0] + 2, _obj.shape[1] + 2, _obj.shape[2]), dtype=np.float32)
    enlarged[1:-1, 1:-1] = _obj
    return enlarged


def prepare_fruit(_f: FruitRecord, data_path: str, input_size):
    _header, _data = _f.load(data_path, is_already_referenced=True)
    _data = cv2.resize(_data, dsize=input_size, interpolation=cv2.INTER_CUBIC)
    _data = np.array(_data)
#    _data = add_border(_data)

    return bands_as_first_dimension(_data)

def bands_as_first_dimension(_obj):
    if isinstance(_obj, torch.Tensor):
        return _obj.permute(2, 0, 1)
    else:
        return _obj.transpose((2, 0, 1))


def bands_as_first_dimension_rev(_obj):
    if isinstance(_obj, torch.Tensor):
        return _obj.permute(1, 2, 0)
    else:
        return _obj.transpose((1, 2, 0))
