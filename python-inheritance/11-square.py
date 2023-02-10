#!/usr/bin/python3
"""
Exercise 11: make a class like the one in
exercise 10, and add its string representation.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Rectangle with equal sides.
    has an implmented 'area' method,
    and its own string representation.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return f"[Square] {self.__width}/{self.__height}"
