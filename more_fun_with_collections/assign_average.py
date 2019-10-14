"""
Program: assign_average.py
Author: Colten Pfander
Last date modified: 10/14/2019

The purpose of this program is to implement a switch/case using a dictionary and function.
"""


def switch_average(key):
    switch_dictionary = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 50}
    try:
        return switch_dictionary.get(key, "Invalid key, try again!")
    except ValueError:
        print("Invalid key, try again!")
    except KeyError:
        print("Invalid key, try again!")


if __name__ == '__main__':
    print(switch_average("G"))
