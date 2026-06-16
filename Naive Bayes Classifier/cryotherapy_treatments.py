import os

from sklearn.metrics import accuracy_score

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
import numpy as np


# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    sample = input().strip().split()
    sample = np.array([float (x) for x in sample])

    class_0 = [row for row in dataset if row[-1] == '0']
    class_1 = [row for row in dataset if row[-1] == '1']

    split_0 = int(len(class_0) * 0.85)
    split_1 = int(len(class_1) * 0.85)

    train = class_0[:split_0] + class_1[:split_1]
    test = class_0[split_0:] + class_1[split_1:]

    train_X = np.array([[float(x) for x in row[:-1]] for row in train])
    train_Y = [int(row[-1]) for row in train]

    test_X = np.array([[float(x) for x in row[:-1]] for row in test])
    test_Y  = [int(row[-1]) for row in test]

    classifier = GaussianNB()
    classifier.fit(train_X,train_Y)

    predictions = classifier.predict(test_X)

    correct = 0
    for y_true, y_pred in zip(test_Y,predictions):
        if y_true == y_pred:
            correct += 1

    accuracy = correct/len(test_Y)

    pred_class = classifier.predict([sample])[0]
    probabilities = classifier.predict_proba([sample])

    print(accuracy)
    print(pred_class)
    print(probabilities)





    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
