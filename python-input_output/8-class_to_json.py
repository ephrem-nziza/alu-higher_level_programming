#!/usr/bin/python3
"""Module that defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of a simple Class instance.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dict, str, int, and bool).

    Returns:
        dict: a dictionary of obj's attribute names and values.
    """
    return obj.__dict__
