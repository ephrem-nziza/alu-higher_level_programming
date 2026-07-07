#!/usr/bin/python3
"""Module that defines search_replace."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list.

    The original list is not modified.
    """
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
