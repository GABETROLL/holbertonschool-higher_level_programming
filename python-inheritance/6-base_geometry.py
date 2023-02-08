#!/usr/bin/python3
"""
Exercise 6: make the 'BaseGeometry' class
in exercise 5 and add an 'area' method to
it.
"""


class BaseGeometry:
    """
    Class with an abstract method 'area'
    """
    def area(self):
        raise NotImplementedError("area() is not implemented")
