#!/usr/bin/python3
"""Module that defines a from_json_string function."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): a JSON string.

    Returns:
        The Python object represented by my_str.
    """
    return json.loads(my_str)
