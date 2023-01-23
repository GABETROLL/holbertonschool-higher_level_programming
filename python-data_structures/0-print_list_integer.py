#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints every integer, assuming they are
    integers, inside the my_list parameter
    each in one line.

    DISCLAIMER: DO NOT USE MUTABLE DEFAULT
    ARGUMENTS LIKE THE my_list PARAMETER,
    UNLESS YOU WANT IT TO BE DEFINED AT FUNCTION
    DEFINITION TIME, AND NOT AT FUNCTION CALL TIME!!!
    """
    for integer in my_list:
        print("{}".format(integer))
