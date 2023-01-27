#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints the first 'x' items in 'my_list',
    not separated by anything, followed by a
    new line.
    If there aren't ehough items to print,
    the function just jumps to printing the
    new line.
    """
    for index in range(x):
        try:
            print(my_list[index])
        except IndexError:
            # ALWAYS put an exception here,
            # otherwise KeyboardInterrupts will not work
            # and we won't know WHAT went wrong, since
            # ALL exceptions are covered when no exception
            # name is given.
            break
    print()
