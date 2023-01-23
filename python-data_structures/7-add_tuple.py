#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    examples:
    add_tuple((0, 3), (4, 5)) -> (4, 8)
    add_tuple((2, 5), (3)) -> (5, 5)
    add_tuple((0), (1)) -> (1, 0)
    add_tuple(2, 3, 4, 5), (6, 7)) -> (2, 10)
    add_tuple() -> (0, 0)

    it only adds the first two items of each
    tuple, with their corresponding indexes,

    it consideres the result (0, 0)
    by default, in case a tuple is empty at
    that index or is None
    """
    result = [0, 0]

    for index in range(2):
        # new way to check if something is None! :)
        if tuple_a and index < len(tuple_a):
            result[index] += tuple_a[index]
        if tuple_b and index < len(tuple_b):
            result[index] += tuple_b[index]

    return tuple(result)
