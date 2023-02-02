#!/usr/bin/python3
"""
Exercise 3: add names with 'say_my_name'
and check its edge cases with doctest
"""


def say_my_name(first_name, last_name=""):
    """
    Makes the person with the first name
    'first_name' and the last name 'last_name'
    introduce themselves like this:

    "My name is <first_name> <last_name>",
    followed by a new line.

    Unless 'first_name' or 'last_name' isn't
    a string.

    If 'last_name' is empty or left default,
    it's treated as a space.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    if not last_name:
        last_name = " "
    print(f"My name is {first_name} {last_name}")
