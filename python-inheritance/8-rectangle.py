#!/usr/bin/python3
"""
Exercise 8: make a 'Rectangle' class that
inherits from 'BaseGeometry'.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry and has
    private width and height fields.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
