#!usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Sets key 'key' in 'a_dictionary' to be paired
    with the value 'value'.

    If the key is already present in the dict,
    it value gets replaced by 'value'.
    This is just how dicts work
    """
    a_dictionary[key] = value
