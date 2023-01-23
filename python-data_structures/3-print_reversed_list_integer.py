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
    for integer in reversed(my_list):
        print("{:d}".format(integer))
