#!/usr/bin/python3
"""
Exercise 1: write, in UTF-8 format,
text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes the contents of 'text' to
    the file called 'filename'.

    If the file doesn't exist, this function
    creates it.

    If the file contains something already,
    this function empties it and writes the
    contents of 'text' into it instead.

    This function returns the result of the
    built-in 'write' method that writes
    to the file.

    (name
    always works like the first exercise,
    unless something in the code is done
    differently)
    """
    with open(filename, "w") as file:
        return file.write(text)
