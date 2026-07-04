#!/usr/bin/python3
"""Module that defines no_c."""


def no_c(my_string):
    """Remove all occurrences of 'c' and 'C' from a string."""
    new_string = ""
    for character in my_string:
        if character != "c" and character != "C":
            new_string += character
    return new_string
