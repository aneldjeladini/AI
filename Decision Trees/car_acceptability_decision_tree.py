import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset


if __name__ == '__main__':
    data = read_file('../data/car.csv')

    encoder = OrdinalEncoder()

    split_index = int(len(data) * 0.7)

    encoder.fit(row[:-1] for row in data)

    train_set = data[:split_index]
    test_set = data[split_index:]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(train_x,train_y)

    preds = classifier.predict(test_x)

    accuracy = accuracy_score(test_y,preds)
    print(f'Tochnost: {accuracy}')
    print(f'Dlabochina: {classifier.get_depth()}')
    print(f'Broj na listovi: {classifier.get_n_leaves()}')
    print(f'Vazhnost na karakteristikite: {classifier.feature_importances_}')


    vaznosti = list(classifier.feature_importances_)
    najvazna_idx = vaznosti.index(max(vaznosti))
    najnevazna_idx = vaznosti.index(min(vaznosti))

    train_x2 = []
    train_x3 = []

    for row in train_x:
        filter_najvazna = [row[i] for i in range(len(row)) if i != najvazna_idx]
        train_x2.append(filter_najvazna)

        filter_najnevazna = [row[i] for i in range(len(row)) if i != najnevazna_idx]
        train_x3.append(filter_najnevazna)

    test_x2 = []
    test_x3 = []

    for row in test_x:
        filter_najvazna = [row[i] for i in range(len(row)) if i != najvazna_idx]
        test_x2.append(filter_najvazna)

        filter_najnevazna = [row[i] for i in range(len(row)) if i != najnevazna_idx]
        test_x3.append(filter_najnevazna)


    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(train_x2,train_y)

    classifier3 = DecisionTreeClassifier(criterion='entropy',random_state=0)
    classifier3.fit(train_x3,train_y)

    preds_2 = classifier2.predict(test_x2)
    accuracy2 = accuracy_score(test_y,preds_2)

    preds_3 = classifier3.predict(test_x3)
    accuracy3 = accuracy_score(test_y,preds_3)

    print(f'Tochnost so otstranuvanje na najvaznata karakteristika: {accuracy2}')
    print(f'Dlabochina so otstraneta najvazna karakteristika: {classifier2.get_depth()}')
    print(f'Broj listovi so otstraneta najvazna karakteristika: {classifier2.get_n_leaves()}')

    print(f'Tochnost (so otstraneta najnevazna karakteristika): {accuracy3}')
    print(f'Dlabochina (so otstraneta najnevazna karakteristika): {classifier3.get_depth()}')
    print(f'Broj na listovi (so otstraneta najnevazna karakteristika): {classifier3.get_n_leaves()}')




























