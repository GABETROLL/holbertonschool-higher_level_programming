#!/usr/bin/python3
"""
Make a class called 'Base'.
"""
from json import dumps


class Base:
    """
    ('Base' is a very vague name, in my opinion,
    you should consider a better name for your
    classes)

    creates a new instance with its individual
    id, that represents how much instances of it
    have been made before it, and itself.

    '__nb_objects' counts the amount of instances
    made since the start of the script.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string format of
        'list_dictionaries', assuming that
        'list_dictionaries' is a list of dictionaries
        ...
        or None, which will result in "[]".
        """
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)
