import io
import json
import unittest
from unittest.mock import patch
from project2 import print_json

class TestPrintJson(unittest.TestCase):

    def test_print_json(self):
        predicted_cuisine = "Italian"
        cuisine_score = 0.95
        closest_cuisines = [(1, 0.9), (2, 0.8)]
        expected_output = {
            'cuisine': predicted_cuisine,
            'score': cuisine_score,
            'closest': [{'id': 1, 'score': 0.9}, {'id': 2, 'score': 0.8}]
        }
        
        # Redirect stdout to a StringIO object
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            # Call the function
            print_json(predicted_cuisine, cuisine_score, closest_cuisines)
            # Get the printed output
            printed_output = mock_stdout.getvalue().strip()
            # Parse the printed output as JSON
            actual_output = json.loads(printed_output)
        
        # Check that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
