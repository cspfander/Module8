"""
Program: set_membership.py
Author: Colten Pfander
Last date modified: 10/14/2019

The purpose of this program is to create a function called in_set that will accept a set and return a boolean stating
if the element is in the set.
"""


def in_set(a_set):
    my_set = set(a_set)
    if a_set == my_set:
        return True
    if a_set != my_set:
        return False


if __name__ == '__main__':
    b_set = {1, 2, 3}
    b_list = [1, 2, 3]
    print(in_set(b_set))    # Example of a set being passed
    print(in_set(b_list))   # Example of a non set being passed
