#!/usr/bin/python3
"""
Exercise 2: Write to a file at the end
of its previous existing contents (aka:
'append')"""


def append_write(filename="", text=""):
    """
    Uses built-ins called 'open' and
    'write' to append the argument called
    'text' into the file called 'filename'.

    If the file doesn't exist, the 'open'
    built-in creates it before writing to
    it.

    This function returns the result of
    'write', which is an int.
    """
    with open(filename, "a") as file:
        return file.write(text)
