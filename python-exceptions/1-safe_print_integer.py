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
    except (TypeError, ValueError) as error:
        # when handling multiple errors in one
        # code block, Python requires us to
        # separate them by commas, inside
        # parenthesis and to use the 'as'
        # keyword to use the exception object.

        # I _THINK_ it's because Python wants
        # to make sure that you know EXACTLY
        # which error was.

        # 'format' raises TypeError for NoneType,
        # tuple and list types, but ValueError
        # when given a string
        return False
    return True
