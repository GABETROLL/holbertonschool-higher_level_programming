#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints the first 'x' items in 'my_list',
    not separated by anything, followed by a
    new line, then returns the amount of elements
    printed.
    If there aren't ehough items to print,
    the function just jumps to printing the
    new line.
    """
    amount_of_elements_printed = 0
    for index in range(x):
        try:
            print(my_list[index], end="")
        except IndexError:
            # ALWAYS put an exception here,
            # otherwise KeyboardInterrupts will not work
            # and we won't know WHAT went wrong, since
            # ALL exceptions are covered when no exception
            # name is given.
            amount_of_elements_printed = index
            break
    else:
        # This code block is only ran if the
        # for loop finished without breaking,
        # and therefore, printed all x elements
        # asked for.
        amount_of_elements_printed = x
    print()
    return amount_of_elements_printed
