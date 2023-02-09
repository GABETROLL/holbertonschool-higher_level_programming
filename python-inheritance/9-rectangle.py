#!/usr/bin/python3
"""
Exercise 9: make a 'Rectangle' class based on
exercise 8 and add an 'area' method that must
BE IMPLEMENTED, along with its string representation.
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

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Returns the area of 'self', according
        to geometry.
        """
        return self.__width * self.__height
