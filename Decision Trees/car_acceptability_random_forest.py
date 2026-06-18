import csv

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset

if __name__ == '__main__':
    dataset = read_file('car.csv')

    encoder = OrdinalEncoder()
    encoder.fit(row[:-1] for row in dataset)

    split_index = int(len(dataset) * 0.70)

    train_set = dataset[:split_index]
    test_set = dataset[split_index:]

    train_x = [row[:-1] for row in train_set]
    train_x = encoder.transform(train_x)
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_x = encoder.transform(test_x)
    test_y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=150, criterion='entorpy', random_state=0)
    classifier.fit(train_x,train_y)

    preds = classifier.predict(test_x)
    accuracy = accuracy_score(test_y,preds)

    print(f'Tochnost: {accuracy}')

    feature_importances = list(classifier.feature_importances_)
    print(f'Vaznost na karakteristiki: {feature_importances}')

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f'Najvazna karakteristika: {most_important_feature}')

    least_important_feature = feature_importances.index(min(feature_importances))
    print(f'Najnevazna karakteristika: {least_important_feature}')


    # прецизност = TP / (TP + FP)
    # одзив = TP / (TP + FN)
    # ф1 = (2 * прецизност * одзив) / (прецизност + одзив)
    # TP - број на точно предвидена класа 1
    # FP - број на грешно предвидена класа 1
    # TN - број на точно предвидена класа 0
    # FN - број на грешно предвидена класа 0

    tp,fp,tn,fn = 0,0,0,0
    for pred, true_y in zip(preds,test_y):
        if pred == 1 and true_y == 1:
            tp += 1
        elif pred == 0 and true_y == 0:
            tn += 1
        elif pred == 1 and true_y == 0:
            fp += 1
        elif pred == 0 and true_y == 1:
            fn += 1

    ac = (tp + tn) / (tp + fp + tn + fn)
    pr = tp / (tp + fp)
    re = tp / (tp + fn)
    f1 = (2 * pr * re) / (pr + re)
    print(f'Preciznost: {pr}')
    print(f'Odziv: {re}')
    print(f'F1: {f1}')



