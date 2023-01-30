#!/usr/bin/python3
"""
How to create a class named 'Square'
with a private attribute 'size'
(aka: '__size')
"""


class Square:
    """
    Square: has private attribute 'size'
    """
    def __init__(self, size):
        self.__size = size
