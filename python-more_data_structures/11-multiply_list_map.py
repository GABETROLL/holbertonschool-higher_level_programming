#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """
    returns new list that's like 'my_list',
    but has all its items multiplied by 'number'

    The challenge here is to use 'map'
    """
    if my_list is None:
        return
    # maps CAN be empty!!!
    # but not None
    return map(my_list, lambda x: x * 2)
