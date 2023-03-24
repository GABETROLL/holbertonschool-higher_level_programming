#!/usr/bin/python3
"""
Exercise 11: Write a 'Student' class like the one
in '10-student.py' (I just copied it).
Add a method, 'reload_from_json(self, json)'
"""


class Student:
    """
    Has a first name (str),
    last name (str)
    and age (int),
    and two methods, 'to_json' and 'reload_from_json',
    that converts 'self' to a dictionary and mutates
    self to have the same fields as a dictionary.

    All the fields in this class are serializable.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        If 'attrs' is None:
        Returns the dict representation of 'self's
        fields. (Their values are all JSON serializable)
        Else:
        Returns the dict representation of 'self's
        fields, as long as the attr names are in 'attrs'.
        If an attr is not a field in 'self', KeyError is raised.
        """
        if attrs:
            for attr in attrs:
                if attr not in self.__dict__:
                    raise KeyError("attr doesn't exist!!!")
                result[attr] = self.__dict__[attr]
        else:
            result = self.__dict__

        return result

    def reload_from_json(self, json):
        """
        Always assuming that 'json' is a dict,
        sets all fields of 'self' named to each
        key in the 'json' arg
        to the values in the 'json' arg.

        If the key is not a field name in 'self',
        KeyError is raised with the message:
        "Invalid attribute for 'Student' object'.
        """
        for field_name, value in json.items():
            if field_name not in self.__dict__:
                raise KeyError("invalid attribute for 'Student' object")
            self.__setattr__(field_name, value)
