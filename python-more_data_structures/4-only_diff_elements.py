#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Returns the set of all the items that
    only show up in one of the two set
    parameters
    """
    return set_1.difference(set_2)
