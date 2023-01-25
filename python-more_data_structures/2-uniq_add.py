#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all items in 'my_list', assuming
    that it's an iterable, without adding the
    same item more than once if it shows up more
    than once in 'my_list'.
    """
    # 'set(my_list)' contains all items
    # in 'my_list', assuming it's an iterable,
    # without repeating the same value multiple
    # times.

    # 'sum' adds all items in the 'set(my_list)'
    # iterable.
    return sum(set(my_list))
