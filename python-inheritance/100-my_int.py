#!/usr/bin/python3
"""
Make an 'int' child class
with its "!=" and "==" swapped!!! :)

cuz why not
"""


class MyInt(int):
    """
    A very naughty 'int' child
    class with its
    "==" and "!=" operators swapped
    !!!
    """
    def __eq__(self, __x: object) -> bool:
        return super().__ne__(__x)

    def __ne__(self, __x: object) -> bool:
        return super().__eq__(__x)
