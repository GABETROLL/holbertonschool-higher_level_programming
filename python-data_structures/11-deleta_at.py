#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Copies the list 'my_list' then
    deletes the item at index 'idx' in
    list 'my_list', and slides all the remaining
    elements into its place (like a soda fridge queue)

    The challenge is to do this without using
    'list.pop'

    If 'my_list' is None, or idx is outside of the
    list's range or negative, this function just returns
    the original list.
    """
    if my_list is None or not (0 <= idx < len(my_list)):
        return my_list

    new_list = list(my_list)
    del new_list[idx]

    return new_list
