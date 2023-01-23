#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    DISCLAIMER: MUTABLE DEFAULT ARGUMENTS LIKE
    'my_list' ARE DEFINED AT FUNCTION DEFINITION
    TIME, AND NOT AT FUNCTION CALL TIME!!!

    THIS MEANS RUNNING THIS FUNCTION MULTIPLE TIMES
    DOES... THINGS...

    Prints each element in the reverse of 'my_list',
    one in each line, assuming all items in
    'my_list' are integers.
    """
    if my_list is None:
        return
    # exit function if my_list is None
    # when checking if a value is None,
    # it's faster to use "is" instead of "==",
    # because all None objects are actually
    # the same object. "==" uses "is" under the
    # hood, and, so, we should just use "is"
    # explicitly, and it also doesn't obfuscate
    # the code at all! :)

    for integer in reversed(my_list):
        print("{:d}".format(integer))
