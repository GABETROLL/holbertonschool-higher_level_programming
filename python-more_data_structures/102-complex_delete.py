#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """
    Deletes all key-value pairs that contain the value
    'value' in the dictionary 'a_dictionary'

    Assuming that the a_dictionary has
    obj[key] -> value functionality.
    """
    # Must make a copy of a_dictionary's key-value
    # pairs FIRST, as, dict.items() doesn't copy them,
    # it just views them. If we delete all the keys
    # that have a value while we're iterating through
    # the viewer, we'll get an error that prevents us
    # from repeating values.
    # Tuples just so happen to run faster and take less
    # memory than lists here, as I only need to copy the
    # values, and not modify them like in a list.
    for key, dict_value in tuple(a_dictionary.items()):
        if dict_value == value:
            del a_dictionary[key]
