#!/usr/bin/python3
"""Module that defines new_in_list."""


def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position.

    Returns a new list; the original list is not modified.
    If idx is negative or out of range, return a copy of my_list.
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
