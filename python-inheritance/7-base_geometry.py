#!/usr/bin/python3
"""
Exercise 7: make the 'BaseGeometry' class
in exercise 6 and add an 'integer_validator'
method to it.
"""


class BaseGeometry:
    """
    Class with an abstract (I'm guessing)
    method 'area'
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Assumes that 'name' is always a string.
        Throws an error if 'value' isn't an integer.
        Throws an error if 'value' is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
