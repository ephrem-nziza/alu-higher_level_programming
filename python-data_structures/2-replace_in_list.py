#!/usr/bin/python3
"""Module that defines replace_in_list."""


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position.

    If idx is negative or out of range, return the list unmodified.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
