#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Makes a new list of length 'list_lenght'.

    Tries to divide the first 'list_length' items in
    list 'my_list_1' by the first 'list_length' in their
    corresponding indexes in 'my_list_2', and places
    the results in the corresponding indexes in the new
    list.

    If the items can't be divided, cause a division
    by 0 if they are divided, or if the index in the
    range of [0, list_length) is bigger than one or
    two lists, the item in the returned array is a 0.

    When the items can't be divided, this function prints
    out "wrong type".
    When the item in the second list is a 0, this function
    prints out "division by 0"
    When the index count has gone too far from the length
    of the lists, this function prints out "out of range"

    (The challenge here is to use 'try', 'except' and
    'finally')

    Then, this function returns the new list.
    """
    result = [0 for _ in range(list_length)]

    for index in range(list_length):
        value_at_index = 0
        try:
            value_at_index = my_list_1[index] / my_list_2[index]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result[index] = value_at_index
    return result
