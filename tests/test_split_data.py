from project2 import split_data
import numpy as np
from sklearn.preprocessing import LabelEncoder

def test_split_data():
    ingredient_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], dtype=np.float32)
    cuisine_labels = np.array(["Italian", "Mexican", "Chinese", "Indian", "Japanese"], dtype=np.str_)
    label_encoder = LabelEncoder()
    cuisine_labels = label_encoder.fit_transform(cuisine_labels)
    
    X_train, _, y_train, _ = split_data(ingredient_array, cuisine_labels)
    
    # Check that the shapes of the returned arrays are correct
    assert X_train.shape == (4, 3)
    assert y_train.shape == (4,)
    
    # Check that the split is randomized
    assert not np.allclose(X_train, ingredient_array[:4])
    assert not np.allclose(y_train, cuisine_labels[:4])
    
    # Check that the split ratio is correct
    assert X_train.shape[0] == int(ingredient_array.shape[0] * 0.8)
    assert y_train.shape[0] == int(cuisine_labels.shape[0] * 0.8)
