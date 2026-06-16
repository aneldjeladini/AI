import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka

    X = int(input().strip())
    sample = input().strip().split()

    split_idx = int(len(dataset) * X / 100)

    train = dataset[:split_idx]
    test = dataset[split_idx:]

    train_X = [row[:-1] for row in train]
    train_Y = [row[-1] for row in train]

    test_X = [row[:-1] for row in test]
    test_Y = [row[-1] for row in test]

    encoder = OrdinalEncoder()
    encoder.fit(train_X)

    train_X_enc = encoder.transform(train_X)
    test_X_enc = encoder.transform(test_X)

    classifier = CategoricalNB()
    classifier.fit(train_X_enc, train_Y)

    correct = 0

    for x, y in zip(test_X_enc, test_Y):
        pred = classifier.predict([x])[0]
        if pred == y:
            correct += 1

    accuracy = correct / len(test_Y)

    sample_enc = encoder.transform([sample])

    predicted_class = classifier.predict(sample_enc)[0]
    probabilities = classifier.predict_proba(sample_enc)

    print(accuracy)
    print(predicted_class)
    print(probabilities)


# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
submit_train_data(train_X_enc, train_Y)

# submit na testirachkoto mnozestvo
submit_test_data(test_X_enc, test_Y)

# submit na klasifikatorot
submit_classifier(classifier)

# submit na encoderot
submit_encoder(encoder)
