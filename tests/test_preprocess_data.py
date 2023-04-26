from project2 import preprocess_data

def test_preprocess_data():
    input_string = 'banana water 23() chicken krispies'
    actual = preprocess_data(input_string)
    expected = 'banana water chicken krispies'
    assert actual == expected