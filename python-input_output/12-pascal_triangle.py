#!/usr/bin/python3
"""Module that defines a pascal_triangle function."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): the number of rows to generate.

    Returns:
        list: a list of lists of integers, or an empty list if
        n is less than or equal to 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
