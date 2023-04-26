
from project2 import train_model
from sklearn.neighbors import KNeighborsClassifier

def test_train_model():

    X_train = [[0, 0], [1, 1]]
    y_train = [0, 1]
    n_neighbors = 1

    k_classifier = train_model(X_train, y_train, n_neighbors)

    # Test that the classifier is an instance of KNeighborsClassifier
    assert isinstance(k_classifier, KNeighborsClassifier)

    # Test that the classifier has been trained on the training data
    assert k_classifier._fit_X.tolist() == X_train

    # Test that the classifier has been trained on the target labels
    assert k_classifier._y.tolist() == y_train

