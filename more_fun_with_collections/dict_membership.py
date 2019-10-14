"""
Program: dict_membership.py
Author: Colten Pfander
Last date modified: 10/14/2019

The purpose of this program is to create a function called in_dict that will accept a dict and return a boolean stating
if the element is in the dict.
"""


def in_dict(a_dict, a_value):
    return a_value in a_dict


if __name__ == '__main__':
    my_dict = {"A": 90, "B": 80, "C": 70}
    value = "A"
    print(in_dict(my_dict, value))
    value = "D"
    print(in_dict(my_dict, value))
