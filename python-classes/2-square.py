#!/usr/bin/python3
"""
How to create a 'Square' class
with a private attribute 'size' that
MUST be an integer, and with an optional
initilazition parameter
"""


class Square:
    """
    A 'Square' class with a private attribute
    'size'.

    'size' MUST be an integer and CAN'T be negative.
    If 'size' is not an 'int' instance, TypeError is raised.
    If 'size' is negative, ValueError is raised.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
