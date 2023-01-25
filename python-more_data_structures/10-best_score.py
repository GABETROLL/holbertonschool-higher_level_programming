#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Returns key with the biggest value.

    Assumes that the values can be compared
    with the one adjacent to them (except
    the first and last)
    """
    # dictionaries loop over their KEYS when iterated
    return max(a_dictionary, key=lambda k: a_dictionary[k])
