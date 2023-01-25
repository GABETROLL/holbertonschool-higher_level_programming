#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Returns key with the biggest value.

    Assumes that the values can be compared
    with the one adjacent to them (except
    the first and last)
    """
    # 'max' doesn't allow empty iterables or None
    if not a_dictionary:
        return
    # dictionaries loop over their KEYS when iterated
    return max(a_dictionary, key=lambda k: a_dictionary[k])
