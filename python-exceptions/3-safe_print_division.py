#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Prints and returns 'a / b'.
    If 'a / b' causes a ZeroDivisionError,
    this function prints None and returns
    None.

    The challenge here is to use 'try',
    'except' and 'finally'.
    """
    value = None
    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        # always runs, even when an exception
        # occurs, which in that case, it runs
        # before exiting.
        print("{}".format(value))
    return value
