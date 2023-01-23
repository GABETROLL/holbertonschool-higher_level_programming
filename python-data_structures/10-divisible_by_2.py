#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Returns list with boolean values that
    correspond to each number in the 'my_list'
    list: True they're even, False if they're odd

    If my_list is None, it returns None

    If my_list is an empty list, it returns
    an empty list
    """
    if my_list is None:
        return
    return [num % 2 == 0 for num in my_list]
