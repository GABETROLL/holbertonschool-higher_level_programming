#!/usr/bin/python3
"""
Exercise 10: Write a 'Student' class like the one
in '9-student.py' (I just copied it) and in the
'to_json' method:
Add an 'attrs' parameter, which should contain
either None or a list of attr names, which will
be the ONLY ONES contained in the dictionary.
If the list is None, just return the expected
dict.
"""


class Student:
    """
    Has a first name (str),
    last name (str)
    and age (int),
    and a 'to_json' JSON representation with
    specific fields.
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
