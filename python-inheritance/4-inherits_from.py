#!/usr/bin/python3
"""
How to know if the class of an instance
inherited from another class
"""

def inherits_from(obj, a_class):
    """
    Returns True if 'obj' is the instance
    of a class that inherits from 'a_class',
    False otherwise.
    """
    return isinstance(obj, a_class)