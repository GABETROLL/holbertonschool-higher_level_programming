#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    ASSUMING that the 'my_list' parameter is an
    iterable (although Holberton's exercise
    specifically uses lists), and that 'search' and 'replace'
    can be compared for equality:

    Returns copy of 'my_list' where each item
    in the new copy that's equal to 'search' gets
    replaced by 'replace'
    """
    return [replace if i == search else i for i in my_list]
