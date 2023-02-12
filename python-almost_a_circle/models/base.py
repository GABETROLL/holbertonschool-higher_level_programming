#!/usr/bin/python3
"""
Exercise 0: Make a class called 'Base'.
"""


class Base:
    """
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
