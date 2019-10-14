"""
Program: assign_average.py
Author: Colten Pfander
Last date modified: 10/14/2019

The purpose of this program is to write a function to compute a half birthday
"""
from datetime import timedelta, date


def a_half_birthday(recent_birthday):
    return recent_birthday + timedelta(days=182.5)


if __name__ == '__main__':
    my_recent_birthday = date(2019, 4, 24)
    print(a_half_birthday(my_recent_birthday))
