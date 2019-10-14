import unittest
from more_fun_with_collections import set_membership as membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        my_set = {1, 2, 3}
        expected_result = True
        self.assertEqual(expected_result, membership.in_set(my_set))

    def test_in_set_false(self):
        my_non_set = [1, 2, 3]
        expected_result = False
        self.assertEqual(expected_result, membership.in_set(my_non_set))


if __name__ == '__main__':
    unittest.main()
