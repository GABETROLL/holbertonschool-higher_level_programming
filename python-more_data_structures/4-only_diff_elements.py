#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Returns the set of all the items that
    only show up in one of the two set
    parameters
    """
    # the set of the items that are only in set_1
    # and the set of the items that are only in set_2
    only_in_set_1 = set_1.difference(set_2)
    only_in_set_2 = set_2.difference(set_1)

    return only_in_set_1.union(only_in_set_2)
