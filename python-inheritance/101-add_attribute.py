#!/usr/bin/python3
"""
Exercise 101: make a function that adds
an attribute to an object "if possible"
"""


def add_attribute(object, name, value):
    """
    Adds attribute named 'name' with
    the value 'value' to the object
    'object'.
    """
    try:
        object.__setattr__(name, value)
    except AttributeError:
        raise TypeError("[TypeError] can't add new attribute")
