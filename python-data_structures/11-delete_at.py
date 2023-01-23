#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
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
    Deletes the item at index 'idx' in
    list 'my_list', and slides all the remaining
    elements into its place
    (like a soda fridge queue)

    THEN RETURNS the (same) my_list
    (due to the fact that by "passing" and
    "returning" data structures, or any
    'object' in Python, we're "passing"
    the pointer to that object around in memory
    (probably?)

    The challenge is to do this without using
    'list.pop'

    If 'my_list' is None, or idx is outside of the
    list's range or negative, this function just skips
    (read above) to returning the original list.
    """
    if my_list and 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
