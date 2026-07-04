#!/usr/bin/python3
"""Module that defines element_at."""


def element_at(my_list, idx):
    """Retrieve an element from a list like in C.

    If idx is negative or out of range, return None.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
