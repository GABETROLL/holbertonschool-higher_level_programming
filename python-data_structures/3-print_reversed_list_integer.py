#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    DISCLAIMER: MUTABLE DEFAULT ARGUMENTS LIKE
    'my_list' ARE DEFINED AT FUNCTION DEFINITION
    TIME, AND NOT AT FUNCTION CALL TIME!!!

    THIS MEANS THE LIST ABOVE IS PUT INTO MEMORY
    WHEN THIS FUNCTION GETS DEFINED,
    AND EVERY TIME THIS FUNCTION IS CALLED WITH
    THE DEFAULT PARAMETER, THE LOADED PARAMETER
    WILL BE THE SAME LIST LOADED THE LAST TIME,
    AND NOT A NEW LIST. THIS CAN HAVE THE PREVIOUS
    CALLS AFFECT THE EMPTY LIST BY THE TIME THE
    CURRENT CALL RUNS.

    FOR A CLEARER EXPLANATION, VISIT:
    https://docs.python-guide.org/writing/gotchas/

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
