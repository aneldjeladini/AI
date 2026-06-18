import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.tree import *
from sklearn.metrics import accuracy_score
from dataset_script import dataset


if __name__ == '__main__':

    split_index = int(len(dataset) * int(input()) / 100)
    criteria = input()
    max_leaves = int(input())

    train_set = dataset[:split_index]
    test_set = dataset[split_index:]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier_1 = DecisionTreeClassifier(criterion=criteria, max_leaf_nodes=max_leaves,random_state=0)
    classifier_1.fit(train_x,train_y)

    preds_1 = classifier_1.predict(test_x)
    accuracy_1 = accuracy_score(test_y,preds_1)

    classes = ['Perch', 'Roach', 'Bream']
    trees = {}

    for fish_class in classes:
        binary_y = [1 if y == fish_class else 0 for y in train_y]

        tree = DecisionTreeClassifier(
            criterion=criteria,
            max_leaf_nodes=max_leaves,
            random_state=0
        )

        tree.fit(train_x, binary_y)
        trees[fish_class] = tree

    correct = 0

    for x, true_class in zip(test_x, test_y):
        valid = True

        for fish_class in classes:
            pred = trees[fish_class].predict([x])[0]

            expected = 1 if true_class == fish_class else 0

            if pred != expected:
                valid = False
                break

        if valid:
            correct += 1

    accuracy_2 = correct / len(test_y)

    print(f'Tochnost so originalniot klasifikator: {accuracy_1}')
    print(f'Tochnost so kolekcija od klasifikatori: {accuracy_2}')

