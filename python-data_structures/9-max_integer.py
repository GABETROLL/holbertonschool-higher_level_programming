#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds and returns the biggest item
    in my_list. If my_list is None or empty,
    this function returns None.

    Assumes all the items in my_list are
    of type 'int', or, more specifically,
    any type that supports the '>' and '<'
    operators.
    """
    # third way to check if something is False
    # it takes the boolean form of the 'my_list'
    # variable! :)
    # if the my_list is empty, it's boolean
    # form is also False!!!
    if not my_list:
        return

    max_int = None
    for next_int in my_list:
        if next_int > max_int or max_int is None:
            max_int = next_int
