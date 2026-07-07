#!/usr/bin/python3
"""Module that defines divisible_by_2."""


def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating multiples of 2.

    Each position matches the original list: True if the integer
    at that position is a multiple of 2, False otherwise.
    """
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
