#!/usr/bin/python3
"""
Exercise 8: convert any object, assuming of its
attributes are serializable, into a JSON string.
"""


def class_to_json(obj):
    """
    Returns the JSON stirng form of the object
    'obj', assuming that all of its attributes
    are serializable.
    """
    return str(obj.__dict__)
