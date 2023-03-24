#!/usr/bin/python3
"""
Exercise 9: Write a Student class with a method
that turns its objects into a dictionary.
(all its fields will be JSON-serializable)
"""


class Student:
    """
    Has a first name (str),
    last name (str)
    and age (int),
    and a 'to_json' JSON representation.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dict representation of 'self's
        fields. (Their values are all JSON serializable)
        """
        return self.__dict__
