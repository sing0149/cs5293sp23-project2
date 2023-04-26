import io
import json
import unittest
from unittest.mock import patch
from project2 import print_json

class TestPrintJson(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_json(self, mock_stdout):
        predicted_cuisine = "Italian"
        cuisine_score = 0.95
        closest_cuisines = [(1, 0.9), (2, 0.8)]
        print_json(predicted_cuisine, cuisine_score, closest_cuisines)
        expected_output = json.dumps({
            'cuisine': predicted_cuisine,
            'score': cuisine_score,
            'closest': [{'id': 1, 'score': 0.9}, {'id': 2, 'score': 0.8}]
        }) + '\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
