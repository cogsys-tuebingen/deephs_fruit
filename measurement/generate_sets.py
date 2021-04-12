from core.fruit_list import *
from core.name_convention import *
from core.hyperspectral_dataset import merge_ripeness_levels

def to_str_entry(e: FruitRecord):
    # FruitRecord(Fruit.KIWI, Side.FRONT, Day.DAY_M2_8, ID.ID_67, CameraType.VIS)
    return f"FruitRecord(Fruit.{e.fruit.name}, Side.{e.side.name}, Day.{e.day.name}, ID.{e.id.name}," \
           f" CameraType.{e.camera_type.name})"


def select_elements(records, select_n):
    selected_elements = np.array([])

    for r in [RipenessState.UNRIPE, RipenessState.PERFECT, RipenessState.OVERRIPE]:
        records_with_state = get_fruits_with_state(records, r)

        selected_elements = np.concatenate([selected_elements,
                                            np.random.choice(records_with_state, int(np.ceil(select_n / 3)),
                                                             replace=False)])
    return selected_elements


if __name__ == '__main__':
    ratio_val = 1 / 8
    ratio_test = 1 / 8

    val_set_elements = np.array([])
    test_set_elements = np.array([])

    for fruit in Fruit:
        for camera_type in CameraType:
            if camera_type == CameraType.RGB:
                # ignore the rgb recordings
                continue

            print(f"##{fruit}: {camera_type}")

            records = get_for_camera_type(get_for_fruit(all_fruits, fruit), camera_type)
            records = get_labeled_fruits(records)
            records = merge_ripeness_levels(records)

            print("N : %i " % len(records))
            n = len(records)

            for r in RipenessState:
                print("%s : %i" % (r.value, len(get_fruits_with_state(records, r))))

            print(f"Select elements evenly with the {ratio_test} ratio of all ripeness levels for test_set..")
            select_n = np.ceil(n * ratio_test)
            selected_elements = select_elements(records, select_n)
            print("selected N  (test): %i " % len(selected_elements))
            test_set_elements = np.concatenate([test_set_elements, selected_elements])
            records = np.delete(records, [records.index(e) for e in selected_elements])

            print(f"Select elements evenly with the {ratio_val} ratio of all ripeness levels for val_set..")
            select_n = np.ceil(n * ratio_val)
            selected_elements = select_elements(records, select_n)
            print("selected N  (val): %i " % len(selected_elements))
            val_set_elements = np.concatenate([val_set_elements, selected_elements])

    print(f"Whole testset size: {len(test_set_elements)}")
    print(f"test_set_fruits = [{', '.join([to_str_entry(e) for e in test_set_elements])}]")

    print(f"Whole valset size: {len(val_set_elements)}")
    print(f"val_set_fruits = [{', '.join([to_str_entry(e) for e in val_set_elements])}]")
