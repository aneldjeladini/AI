import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from dataset_script import dataset

if __name__ == '__main__':

    C = int(input())
    P = int(input())

    class_good = [row for row in dataset if row[-1] == 'good']
    class_bad = [row for row in dataset if row[-1] == 'bad']

    class_good_modified = []
    for row in class_good:
        new_val = row[0] + row[-2]
        new_row = [new_val] + row[1:-2] + [row[-1]]
        class_good_modified.append(new_row)

    class_bad_modified = []
    for row in class_bad:
        new_val = row[0] + row[-2]
        new_row = [new_val] + row[1:-2] + [row[-1]]
        class_bad_modified.append(new_row)

    good_split = int(len(class_good_modified) * P / 100)
    bad_split = int(len(class_bad_modified) * P / 100)

    if C == 0:
        train_set = (
            class_good_modified[:good_split] +
            class_bad_modified[:bad_split]
        )

        test_set = (
            class_good_modified[good_split:] +
            class_bad_modified[bad_split:]
        )
    else:
        good_start = int(len(class_good_modified) * (100 - P) / 100)
        bad_start = int(len(class_bad_modified) * (100 - P) / 100)

        train_set = (
                class_good_modified[good_start:] +
                class_bad_modified[bad_start:]
        )

        test_set = (
                class_good_modified[:good_start] +
                class_bad_modified[:bad_start]
        )

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    # First classifier (without scaling)
    classifier_1 = GaussianNB()
    classifier_1.fit(train_x, train_y)

    preds_1 = classifier_1.predict(test_x)
    accuracy_1 = accuracy_score(test_y, preds_1)

    # Second classifier (with scaling)
    scaler = MinMaxScaler(feature_range=(-1, 1))

    train_x_scaled = scaler.fit_transform(train_x)
    test_x_scaled = scaler.transform(test_x)

    classifier_2 = GaussianNB()
    classifier_2.fit(train_x_scaled, train_y)

    preds_2 = classifier_2.predict(test_x_scaled)
    accuracy_2 = accuracy_score(test_y, preds_2)

    print(f"Tochnost so zbir na koloni: {accuracy_1}")
    print(f"Tochnost so zbir na koloni i skaliranje: {accuracy_2}")