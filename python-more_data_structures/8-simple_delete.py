#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key 'key' from the dictionary
    'a_dictionary' if the key is present.
    """
    # None prevents the pop method raising a
    # KeyError when the key isn't in the dict
    a_dictionary.pop("key", None)
