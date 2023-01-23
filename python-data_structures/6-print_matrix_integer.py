#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    DISCLAIMER: MUTABLE DEFAULT ARGUMENTS LIKE
    'matrix' ARE DEFINED AT FUNCTION DEFINITION
    TIME, AND NOT AT FUNCTION CALL TIME!!!

    THIS MEANS THE LIST ABOVE IS PUT INTO MEMORY
    WHEN THIS FUNCTION GETS DEFINED,
    AND EVERY TIME THIS FUNCTION IS CALLED WITH
    THE DEFAULT PARAMETER, THE LOADED PARAMETER
    WILL BE THE SAME LIST LOADED THE LAST TIME,
    AND NOT A NEW LIST. THIS CAN HAVE THE PREVIOUS
    CALLS AFFECT THE EMPTY LIST BY THE TIME THE
    CURRENT CALL RUNS.

    FOR A CLEARER EXPLANATION, VISIT:
    https://docs.python-guide.org/writing/gotchas/

    Assuming the 'matrix' parameter is a 2d list,
    meaning, a list that contains lists:

    Prints matrix of integers like this example:
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    1 2 3
    4 5 6
    7 8 9

    """
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))
