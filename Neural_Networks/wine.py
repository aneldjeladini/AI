import warnings

warnings.filterwarnings("ignore")

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def read_dataset():
    data = []
    with open('../data/winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data


if __name__ == '__main__':
    dataset = read_dataset()

    dataset_good = [row for row in dataset if row[-1] == 'good']
    dataset_bad = [row for row in dataset if row[-1] == 'bad']

    train_set = dataset_good[:int(len(dataset_good) * 0.70)] + dataset_bad[:int(len(dataset_bad) * 0.70)]
    validation_set = dataset_good[int(len(dataset_good) * 0.70) : int(len(dataset_good) * 0.80)] + dataset_bad[int(len(dataset_bad) * 0.70) : int(len(dataset_bad) * 0.80)]
    test_set = dataset_good[int(len(dataset_good) * 0.80):] + dataset_bad[int(len(dataset_bad) * 0.80):]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    validation_x = [row[:-1] for row in validation_set]
    validation_y = [row[-1] for row in validation_set]

    classifier_1 = MLPClassifier(hidden_layer_sizes=(5,), activation='relu', learning_rate_init=0.001, max_iter=500)
    classifier_2 = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', learning_rate_init=0.001, max_iter=500)
    classifier_3 = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', learning_rate_init=0.001, max_iter=500)

    classifier_1.fit(train_x,train_y)
    classifier_2.fit(train_x,train_y)
    classifier_3.fit(train_x,train_y)

    preds1 = classifier_1.predict(validation_x)
    preds2 = classifier_2.predict(validation_x)
    preds3 = classifier_3.predict(validation_x)

    acc_1 = accuracy_score(validation_y,preds1)
    acc_2 = accuracy_score(validation_y,preds2)
    acc_3 = accuracy_score(validation_y,preds3)

    print(f'Tochnost so 5 nevroni (val): {acc_1}')
    print(f'Tochnost so 10 nevroni (val): {acc_2}')
    print(f'Tochnost so 100 nevroni (val): {acc_3}')

    if acc_1 >= acc_2 and acc_1 >= acc_3:
        print('Najdobar e prviot klasifikator')
        preds = classifier_1.predict(test_x)
    elif acc_2 >= acc_1 and acc_2 >= acc_3:
        print('Najdobar e vtoriot klasifikator')
        preds = classifier_2.predict(test_x)
    else:
        print('Najdobar e tretiot klasifikator')
        preds = classifier_3.predict(test_x)

    acc = accuracy_score(preds, test_y)
    print(f'Tochnost so najdobriot klasifikator (test): {acc}')
