#!/usr/bin/python3
"""
How to write a class that inherits from
the built-in class 'list'.
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
