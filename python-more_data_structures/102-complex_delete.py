#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """
    Deletes all key-value pairs in 'a_dictionary'
    that contain the value 'value' IN PLACE,
    then returns 'a_dictionary'.

    assuming that the a_dictionary has
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
    for old_key, old_value in tuple(a_dictionary.items()):
        if old_value == value:
            del a_dictionary[old_key]
    return a_dictionary
