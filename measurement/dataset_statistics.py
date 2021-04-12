import seaborn as sns
import numpy as np
import pandas
import argparse
import matplotlib.pyplot as plt

from core.name_convention import *
from core.fruit_list import all_fruits_m1, all_fruits, get_for_camera_type, get_for_fruit, get_labeled_fruits
import core.argparser_utils as argparser_utils
from core.hyperspectral_dataset import merge_ripeness_levels, extend_unripe_recordings

def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fruit", type=argparser_utils.str2fruit, required=True)
    parser.add_argument("--camera_type", type=argparser_utils.str2cameratype, required=True)
    opt = parser.parse_args()
    return opt


def get_supervised_dataset(records, fruit, camera_type):
    print("# Total records: %i" % len(records))
    records = get_for_fruit(get_for_camera_type(records, camera_type), fruit)
    print("# Valid records: %i" % len(records))

    _records = get_labeled_fruits(records)
    print("# Labeled records: %i" % len(_records))

    records = extend_unripe_recordings(records)
    records = get_labeled_fruits(records)
    print("# Labeled records (extended): %i" % len(records))

    return records


def get_statistic_df_of(records: [FruitRecord]):
    entries = {
        "id": [],
        "day": [],
        "fruit": [],
        "is_labeled": [],
        "firmness": [],
        "ripeness_level": [],
        "storage_days": [],
        "sweetness": [],
    }

    for r in records:
        entries['id'].append("%s_%s" % (r.id, r.side.value))
        entries['day'].append(r.day)
        entries['fruit'].append(r.fruit.value)
        entries['is_labeled'].append(r.is_labeled())
        entries['firmness'].append(float(r.label.firmness) if r.label.firmness is not None else None)
        entries['ripeness_level'].append(r.label.ripeness_state.value)
        entries['storage_days'].append(r.label.storage_days)
        entries['sweetness'].append(r.label.sugar_content if r.fruit == Fruit.KIWI else 0)

    df = pandas.DataFrame(entries)

    df["id"] = df["id"].astype('category')
    df["day"] = df["day"].astype('category')
    df["fruit"] = df["fruit"].astype('category')
    df["is_labeled"] = df["is_labeled"].astype('category')
    df["ripeness_level"] = df["ripeness_level"].astype('category')

    return df


def get_count_of_rows(df, l):
    _df = df.apply(l, axis=1) == True
    numOfRows = len(_df[_df == True].index)

    return numOfRows


def plot_distribution(df):
    sns.countplot(x="ripeness_level", data=df, order=[r.value for r in[RipenessState.UNRIPE,
                                         RipenessState.RIPE,
                                         RipenessState.PERFECT,
                                         RipenessState.NEAR_OVERRIPE,
                                         RipenessState.OVERRIPE]])
    plt.title("Record distribution")
    plt.show()
    sns.displot(df, x="firmness")
    plt.title("Record distribution")
    plt.show()

    if get_count_of_rows(df, lambda x: x.fruit == Fruit.KIWI.value):
        sns.displot(df, x="sweetness")
        plt.title("Record distribution")
        plt.show()

    # ripness_level_dist = {
    #     "ripeness_level" : [RipenessState.UNRIPE,
    #                                      RipenessState.RIPE,
    #                                      RipenessState.PERFECT,
    #                                      RipenessState.NEAR_OVERRIPE,
    #                                      RipenessState.OVERRIPE],
    #     "count": [get_count_of_rows(df, lambda x: x['ripeness_level'] == rl.value) for rl in [RipenessState.UNRIPE,
    #                                      RipenessState.RIPE,
    #                                      RipenessState.PERFECT,
    #                                      RipenessState.NEAR_OVERRIPE,
    #                                      RipenessState.OVERRIPE]]
    # }
    #
    # sns.boxplot(pandas.DataFrame(ripness_level_dist), x="ripeness_level", y="count")

if __name__ == '__main__':
    opt = get_opt()
    records = all_fruits
    records = get_supervised_dataset(records, opt.fruit, opt.camera_type)
    records = merge_ripeness_levels(records)

    df = get_statistic_df_of(records)
    plot_distribution(df)
