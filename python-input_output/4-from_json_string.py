#!/usr/bin/python3
"""
Exercise 4: make a function that returns
an object from a JSON string.
"""
from json import load


def from_json_string(my_str):
    """
    Returns the object form of the
    'my_str' string, using
    'json.load'.

    I don't know what happens when
    the string's ormat is invalid...
    """
    load(my_str)
