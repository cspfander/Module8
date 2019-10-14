import unittest
from more_fun_with_collections import dict_membership as d_member


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        my_dict = {"A": 90, "B": 80, "C": 70}
        expected_result = True
        self.assertEqual(expected_result, d_member.in_dict(my_dict))

    def test_in_set_false(self):
        my_non_dict = ["A", 90, "B", 80, "C", 70]
        expected_result = False
        self.assertEqual(expected_result, d_member.in_dict(my_non_dict))


if __name__ == '__main__':
    unittest.main()
