#!/usr/bin/python3
"""
Exercise 8: convert any object, assuming of its
attributes are serializable, into a JSON string.
"""


def class_to_json(obj):
    """
    Returns dictionary form of 'obj',
    assuming that its attributes are all
    JSON serializable.
    """
    return obj.__dict__
