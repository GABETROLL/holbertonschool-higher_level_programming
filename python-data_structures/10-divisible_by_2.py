#!/usr/bin/python3


def divisible_by_2(my_list=[]):
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
    Returns list with boolean values that
    correspond to each number in the 'my_list'
    list: True they're even, False if they're odd

    If my_list is None, it returns None

    If my_list is an empty list, it returns
    an empty list
    """
    if my_list is None:
        return
    return [num % 2 == 0 for num in my_list]
