#!/usr/bin/python3
"""
Exercise 0: print the contents of a file,
in UTF-8 format, to the standard output.
"""


def read_file(filename=""):
    """
    Prints the contents of the file
    'filename', in the computer running
    this script, to the standard output,
    in UTF-8 format.

    The name is relative to
    the current working dierctory.
    """
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
