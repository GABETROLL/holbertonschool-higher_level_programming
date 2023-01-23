#!/usr/bin/python3

def element_at(my_list, index):
    """
    Returns element at index 'index'
    in list 'my_list'.

    If the index is negative or out of range,
    it returns None.
    """
    if 0 <= index < len(my_list):
        return my_list[index]
