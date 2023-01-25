#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key 'key' from the dictionary
    'a_dictionary' IN PLACE if the key is present,
    then returns 'a_dictionary'
    """
    # None prevents the pop method raising a
    # KeyError when the key isn't in the dict
    a_dictionary.pop(key, None)
    return a_dictionary
