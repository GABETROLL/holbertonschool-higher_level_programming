#!/usr/bin/python3
"""
How to write a class that inherits from
the built-in class 'list'.
"""


class MyList(list):
    """
    Child class of the Python built-in
    'list' class, with a method to print
    its sorted version.
    """
    def print_sorted(self):
        """
        Prints the sorted version of 'self',
        by creating a new 'list' of 'self'
        using 'sorted', then printing that.
        """
        print(sorted(self))
