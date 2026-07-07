#!/usr/bin/python3
"""Module that defines square_matrix_simple."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.

    Returns a new matrix of the same size; the original is untouched.
    """
    new_matrix = []
    for row in matrix:
        new_row = [value ** 2 for value in row]
        new_matrix.append(new_row)
    return new_matrix
