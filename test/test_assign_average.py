import unittest
from more_fun_with_collections.assign_average import switch_average


class ScoreTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        name = 'A'
        expected_result = 90
        self.assertEqual(expected_result, switch_average(name))

    def test_score_input_test_score_valid(self):
        name = 'B'
        expected_result = 80
        self.assertEqual(expected_result, switch_average(name))

    def test_score_input_test_score_below_range(self):
        name = 'C'
        expected_result = 70
        self.assertEqual(expected_result,
                         switch_average(name))

    def test_score_input_test_score_above_range(self):
        name = 'D'
        expected_result = 60
        self.assertEqual(expected_result,
                         switch_average(name))

    def test_score_non_numeric(self):
        name = 'F'
        expected_result = 50
        self.assertEqual(expected_result,
                         switch_average(name))

    def test_score_input_invalid_message(self):
        name = 'G'
        expected_result = 'Invalid test score, try again!'
        self.assertEqual(expected_result,
                         switch_average(name))


if __name__ == '__main__':
    unittest.main()
