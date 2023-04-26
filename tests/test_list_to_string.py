from project2 import list_to_string 
def test_list_to_string():
    ingredients_list = ['Onion', 'Garlic', 'Ginger']
    expected_output = 'onion garlic ginger'
    assert list_to_string(ingredients_list) == expected_output
    
    ingredients_list = ['Salt', 'Pepper', 'Olive Oil']
    expected_output = 'salt pepper olive oil'
    assert list_to_string(ingredients_list) == expected_output
    
    ingredients_list = ['Chicken', 'Broccoli', 'Soy Sauce']
    expected_output = 'chicken broccoli soy sauce'
    assert list_to_string(ingredients_list) == expected_output
