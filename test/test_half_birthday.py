import unittest
from datetime import datetime
from more_fun_with_collections import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        recent_birthday = datetime.datetime(2019, 4, 24)
        expected_result = datetime.datetime(2019, 10, 23)
        self.assertEqual(expected_result, half_birthday(recent_birthday))


if __name__ == '__main__':
    unittest.main()
