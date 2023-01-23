#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    replaces element at index 'idx' in list
    'my_list' with element 'element' in a new
    COPY of my_list.

    If the index 'idx' is out of range, it just
    returns the copy.
    """
    new_list = list(my_list)

    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
