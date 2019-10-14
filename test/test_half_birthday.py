import unittest
from datetime import date
from more_fun_with_collections.half_birthday import a_half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        recent_birthday = date(2019, 4, 24)
        expected_result = date(2019, 10, 23)
        self.assertEqual(expected_result, a_half_birthday(recent_birthday))


if __name__ == '__main__':
    unittest.main()
