#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Returns copy of dict 'a_dictionary', with
    all of the old dict's values multiplied by 2
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
