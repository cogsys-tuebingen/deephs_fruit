from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import argparse

from core.name_convention import *
import core.fruit_list as fruit_list
from core.hyperspectral_dataset import get_records
from core.hyperspectral_dataset import extract_val_data, extract_test_data



def test_knn_with_fixed_test_set(X_train, y_train, X_test, y_test, silence=False):
    knn = KNeighborsClassifier(metric='euclidean')
    # create a dictionary of all values we want to test for n_neighbors
    param_grid = {'n_neighbors': np.arange(1, 10)}
    # use gridsearch to test all values for n_neighbors
    knn_gscv = GridSearchCV(knn, param_grid, cv=2, iid=False)
    # fit model to data
    knn_gscv.fit(X_train, y_train)
    score = knn_gscv.score(X_test, y_test)

    if not silence:
        print("# [knn] Accuracy is: %.2f %%" % (score * 100))
        print("#\t With n: %i " % knn_gscv.best_params_['n_neighbors'])
    return score


def main(classification_type, fruit, camera_type, data_path):
    train_records, val_records, test_records = get_records(fruit, camera_type, classification_type, use_inter_ripeness_levels=True)

    train_records = np.concatenate([train_records, val_records])

    def load_fruit(r: FruitRecord):
        _, _d = r.load(data_path, True)
        _d = _d.mean(axis=0).mean(axis=0)

        if classification_type == ClassificationType.RIPENESS:
            return _d, ripeness2int(r.label.ripeness_state)
        if classification_type == ClassificationType.FIRMNESS:
            return _d, firmness2int(r.label.get_firmness_level())
        if classification_type == ClassificationType.SUGAR:
            return _d, sugar2int(r.label.get_sugar_level())

    def get_dataset(records):
        X = []
        Y = []
        for _r in records:
            x, y = load_fruit(_r)
            X.append(x)
            Y.append(y)

        X = np.stack(X)
        Y = np.stack(Y)

        return X, Y

    X_train, Y_train = get_dataset(train_records)
    X_test, Y_test = get_dataset(test_records)

    score = test_knn_with_fixed_test_set(X_train, Y_train, X_test, Y_test, True)

    print("# [%s; %s; %s] Avg. accuracy: %f" % (classification_type.value, fruit.value.lower(), camera_type.value.lower(),
                                                score * 100))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "KNN:")
    parser.add_argument("--data_path", type=str, required=True, help="the root folder of dataset")
    opt = parser.parse_args()

    main(ClassificationType.RIPENESS, Fruit.AVOCADO, CameraType.VIS, opt.data_path)
    main(ClassificationType.RIPENESS, Fruit.AVOCADO, CameraType.NIR, opt.data_path)
    main(ClassificationType.RIPENESS, Fruit.KIWI, CameraType.VIS, opt.data_path)
    main(ClassificationType.RIPENESS, Fruit.KIWI, CameraType.NIR, opt.data_path)

    main(ClassificationType.FIRMNESS, Fruit.AVOCADO, CameraType.VIS, opt.data_path)
    main(ClassificationType.FIRMNESS, Fruit.AVOCADO, CameraType.NIR, opt.data_path)
    main(ClassificationType.FIRMNESS, Fruit.KIWI, CameraType.VIS, opt.data_path)
    main(ClassificationType.FIRMNESS, Fruit.KIWI, CameraType.NIR, opt.data_path)

    main(ClassificationType.SUGAR, Fruit.KIWI, CameraType.VIS, opt.data_path)
    main(ClassificationType.SUGAR, Fruit.KIWI, CameraType.NIR, opt.data_path)