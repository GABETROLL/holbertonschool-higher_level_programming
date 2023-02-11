#!/usr/bin/python3
"""
Exercise 6: Make a function that returns
an object from a file with the object's
JSON form.
"""
from json import load


def load_from_json_file(filename):
    """
    returns the object stored in its
    JSON form in the 'filename'
    file parameter in its Python object
    form.

    Please read documentation for the 'dump'
    function and when it raises exceptions:
    https://docs.python.org/3/library/json.html

    If an error occurs while calling
    'load', the file automatically closes
    before the error.

    If 'filename' doesn't exist, FileNotFound
    is raised by 'open'.
    """
    with open(filename, "r") as file:
        return load(file)
