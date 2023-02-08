#!/usr/bin/python3
"""
Exercise 6: make the 'BaseGeometry' class
in exercise 5 and add an 'area' method to
it.
"""


class BaseGeometry:
    """
    Class with an abstract (I'm guessing)
    method 'area'
    """
    def area(self):
        raise Exception("area() is not implemented")
