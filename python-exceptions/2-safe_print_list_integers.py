#!/usr/bin/python3
"""Module that defines safe_print_list_integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, integers only.

    Non-integer values are skipped silently. Returns the number
    of integers actually printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
