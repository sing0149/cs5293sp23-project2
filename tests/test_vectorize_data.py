
from project2 import vectorize_data
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def test_vectorize_data():
    # Create sample data
    clean_data = {'ingredients': ['pasta tomato cheese', 'rice soy sauce chicken', 'sushi rice fish avocado']}
    
    # Create an instance of TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()
    
    # Call the vectorize_data function
    ingredient_matrix, ingredient_array = vectorize_data(clean_data, tfidf_vectorizer)
    
    # Check the shape of the ingredient matrix
    assert ingredient_matrix.shape == (3, 10)
    
    # # Check that the matrix is sparse
    assert np.allclose(ingredient_matrix.toarray(), ingredient_array)
