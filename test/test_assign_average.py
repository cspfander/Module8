import unittest
from more_fun_with_collections.assign_average import switch_average


class ScoreTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        key = 'A'
        expected_result = 90
        self.assertEqual(expected_result, switch_average(key))

    def test_score_input_test_score_valid(self):
        key = 'B'
        expected_result = 80
        self.assertEqual(expected_result, switch_average(key))

    def test_score_input_test_score_below_range(self):
        key = 'C'
        expected_result = 70
        self.assertEqual(expected_result,
                         switch_average(key))

    def test_score_input_test_score_above_range(self):
        key = 'D'
        expected_result = 60
        self.assertEqual(expected_result,
                         switch_average(key))

    def test_score_non_numeric(self):
        key = 'F'
        expected_result = 50
        self.assertEqual(expected_result,
                         switch_average(key))

    def test_score_input_invalid_message(self):
        key = 'G'
        expected_result = 'Invalid key, try again!'
        self.assertEqual(expected_result,
                         switch_average(key))


if __name__ == '__main__':
    unittest.main()
