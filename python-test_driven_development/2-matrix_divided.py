#!/usr/bin/python3
"""
Second (?) exercise to learn doctest
"""


def matrix_divided(matrix, div):
    """
    Returns a new 'matrix' matrix with all its
    elements divided by 'div', then rounded to 2
    decimal places.

    If 'matrix' is not a list of integers or floats,
    TypeError is raised.
    If matrix's rows are not all the same length,
    TypeError is raised.
    If 'div' isn't an 'int' or a 'float',
    TypeError is raised.
    If 'div' is '0',
    ZeroDivisionError is raised.
    """
    INVALID_MATRIX_ERORR_MESSAGE = "matrix must be a matrix \
        (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(INVALID_MATRIX_ERORR_MESSAGE)
    if not (type(div) in (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []

    for row in matrix:
        if type(row) != list:
            raise TypeError(INVALID_MATRIX_ERORR_MESSAGE)

        if result and len(row) != len(result[-1]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for x in row:
            if not (type(x) in (int, float)):
                raise TypeError(INVALID_MATRIX_ERORR_MESSAGE)
            new_row.append(round(x / div), 2)
        result.append(new_row)

    return result
