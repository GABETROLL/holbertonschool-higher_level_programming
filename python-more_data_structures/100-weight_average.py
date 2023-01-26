#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    Returns the weighted average of all the items
    in 'my_list' where each item HAS to be
    a tuple, its 0th item is a score
    and its 1st item is a weight.

    example:
    if my_list == [(1, 2), (2, 1), (3, 10), (4, 2)]
    return (1 * 2) + (2 * 1) + (3 * 10) + (4 * 2))
        / (2 + 1 + 10 + 2)

    If 'my_list' is empty, this function just
    returns 0.
    """
    if not my_list:
        return 0
    a = sum(item[0] * item[1] for item in my_list)
    b = sum(item[1] for item in my_list)
    return a / b
