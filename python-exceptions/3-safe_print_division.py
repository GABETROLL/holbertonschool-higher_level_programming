#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Prints "Inside result:" followed by
    'a / b', then returns 'a / b'.
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
        pass
    finally:
        # always runs, even when an exception
        # occurs, which in that case, it runs
        # before exiting.
        print("Inside result: {}".format(value))
    return value
