"""
Program: dictionary_update.py
Author: Colten Pfander
Last date modified: 10/14/2019

The purpose of this program is to update the code from the assignment Function Default Values with dictionaries.
"""


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    """
    :param test_name: stores user input as a test name to print
    :param test_score: stores a user input as a test score to print as well as be validated (optional)
    :param invalid_message: optional message that displays an indicated string if the user has input an invalid score
    :return: either returns a string with the Test_name : test_score or with an invalid_message for an invalid input
    """
    try:
        int(test_score)
    except ValueError:
        return "Invalid test score! Please use only numeric!"
    if 0 <= int(test_score) <= 100:
        return {test_name: test_score}
    else:
        return invalid_message


def average_scores(a_dict):
    total_score = 0
    for value in a_dict:
        total_score += int(a_dict[value])
    num_of_scores = len(a_dict)
    return total_score / num_of_scores


if __name__ == '__main__':
    num_scores = int(input("Please enter the number of test scores: "))
    scores_dict = dict()
    control_variable = 0
    while control_variable < num_scores:
        a_test_name = input("Please enter the test name: ")
        a_test_score = input("Enter a test score: ")
        score = score_input(a_test_name, a_test_score)
        scores_dict.update(score)
        control_variable += 1
    print(average_scores(scores_dict))  # prints the average of the scores in the dictionary
    print(scores_dict)  # shows what the dictionary contains "test name": test score
