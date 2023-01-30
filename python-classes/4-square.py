#!/usr/bin/python3
"""
How to create property getter and setter methods
for private attribute 'size'
"""


class Square:
    """
    'Square' class that has all of its
    (theoretical) sides' lenghts as a 'size'
    private attribute with its getters and
    setters.

    'size' MUST be an integer and MUST NOT be
    negative.
    """
    def __init__(self, size=0):
        self.__size = None
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the area of the square
        (aka: 'self')
        """
        return self.__size ** 2
