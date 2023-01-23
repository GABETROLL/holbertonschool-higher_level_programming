#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints matrix of integers like this example:

    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    1 2 3
    4 5 6
    7 8 9

    """
    for row in matrix:
        print(" ".join("{:d}".format(row)))
