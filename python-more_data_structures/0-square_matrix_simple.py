#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Returns a copy of the matrix 'matrix' with all its
    integers squared.
    """
    return [[n ** 2 for n in row] for row in matrix]
