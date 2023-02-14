#!/usr/bin/python3
"""
Make a class called 'Base'.
"""
from json import dumps, loads


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

    def to_dictionary(self):
        """
        All of the children of this class
        should be JSON serializable by turning
        their instances into a dictoinary with
        an override of this method.
        """
        raise NotImplementedError("'to_dictionary' isn't implemented in 'Base'")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Assumes that 'list_objs' is a list
        of instances of any class THAT INHERITS
        FROM THIS ONE ('Base'), or 'None'.
        If 'list_objs' is None, it's treated as
        '[]'.

        Assumes that 'cls' is a class that inherits
        from this one ('Base').

        Saves the JSON representation of 'list_objs'
        to a file called f"{cls}.json". If the file
        already exists, it's overriden.
        """
        if list_objs is None:
            list_objs = []

        list_objs = [obj.to_dictionary() for obj in list_objs]

        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """
        Loads JSON object from file named
        f"{cls}.son".
        """
        pass

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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list representation of
        the 'json_string' JSON string.

        If 'json_string' is None or empty,
        an empty list is returned.
        """
        if json_string is None:
            return []
        return loads(json_string)
