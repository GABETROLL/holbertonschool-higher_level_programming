#!/usr/bin/python3
"""
How to make a function that returns
True if an object is an instance of
an EXACT class (and not the class' children),
otherwise, False.
"""


def is_same_class(obj, a_class):
    """
    Returns True if 'obj' is an instance
    of the EXACT class 'a_class' (AND NOT OF
    THE CLASS' CHILDREN), otherwise, False.
    """
    return type(obj) == a_class
