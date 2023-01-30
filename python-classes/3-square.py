#!/usr/bin/python3
"""
How to create create a public
method that uses a private attribute
"""


class Square:
    """
    'Square' class with a private attribute
    'size', that can be used to calculate its
    area
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns this square's area according
        to: A = x ** 2
        """
        return self.__size ** 2
