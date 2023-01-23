#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    replaces element at index 'idx' in list
    'my_list' with element 'element' IN PLACE,
    and returns 'my_list'

    If 'idx' is negative or out of range of
    'my_list', it just returns 'my_list'
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
