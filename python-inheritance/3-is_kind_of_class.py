#!/usr/bin/python3
"""
How to make a function that returns
True if an object is an instance of
a class, including the class' children;
otherwise, False.
"""


def is_same_class(obj, a_class):
    """
    Returns True if 'obj' is an instance
    of 'a_class', or its chidren; otherwise,
    False.
    """
    return isinstance(obj, a_class)
