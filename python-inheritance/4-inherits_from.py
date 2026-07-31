#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class.

    Args:
        obj: the object to check.
        a_class: the base class to compare against.

    Returns:
        bool: True if obj's class inherits from a_class (directly or
        indirectly), but obj is not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
