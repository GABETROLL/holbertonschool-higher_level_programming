#!/usr/bin/python3
"""
Exersice 4 for learning doctest
"""


def print_square(size):
    """
    Prints a 'size' * 'size' square
    made of "#"'s to the standard output.
    
    Unless 'size' isn't an integer or is
    lower than zero."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
