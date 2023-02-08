#!/usr/bin/python3
"""
Contains function for looking-up all
attributes of an object
"""


def lookup(obj):
    """
    Returns a list of all the atributes
    of the object 'obj'.
    """
    return dir(obj)
