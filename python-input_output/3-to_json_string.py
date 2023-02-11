#!/usr/bin/python3
"""
Exercise 3: Write a function that returns
the JSON representaion of an object.
"""
from json import dumps


def to_json_string(my_obj):
    """
    Returns the JSON string
    representation of the object
    argument 'my_obj', using the
    built-in function called
    'json.dumps'.
    """
    return dumps(my_obj)
