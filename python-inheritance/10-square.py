#!/usr/bin/python3
"""
Exercise 10: make a class 'Square' that
inherits from 'Rectangle' in exercise 9,
and has the 'area' method implemented.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Rectangle with equal sides.
    has an implmented 'area' method.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
