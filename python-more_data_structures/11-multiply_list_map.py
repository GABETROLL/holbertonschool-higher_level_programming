#!/usr/bin/python3

# returns new list that's like 'my_list'
# but has all its items multiplied by 'number'

# The challenge here is to use 'map'
# and to write the function in only 3 lines
def multiply_list_map(my_list=[], number=0):
    if my_list is None:
        return
    return map(my_list, lambda x: x * 2)
