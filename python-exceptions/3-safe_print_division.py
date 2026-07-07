#!/usr/bin/python3
"""Module that defines safe_print_division."""


def safe_print_division(a, b):
    """Divide two integers and print the result.

    Returns the division result, or None if a ZeroDivisionError occurs.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
