#!/usr/bin/python3
"""
Exercise 5: Make a function that writes
an to a JSON file, in its JSON form.
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    Writes the object argument called
    'my_obj' to the JSON file argument
    called 'filename' in its JSON form.

    Uses the 'with' statement to automatically
    close the file if an error occurs while
    writing to itm followed by actually raising
    the exception.

    If the file 'filename' doesn't exist,
    an error occurs.
    """
    with open(filename, "w") as file:
        dump(my_obj, file)
