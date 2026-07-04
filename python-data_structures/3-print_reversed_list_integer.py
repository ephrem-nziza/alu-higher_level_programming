#!/usr/bin/python3
"""Module that defines print_reversed_list_integer."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line."""
    for number in reversed(my_list):
        print("{:d}".format(number))
