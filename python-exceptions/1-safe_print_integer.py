#!/usr/bin/python3


def safe_print_integer(value):
    """
    Prints integer 'value'
    Returns True if 'value' was
    an integer, otherwise, doesn't
    print and returns False.
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
