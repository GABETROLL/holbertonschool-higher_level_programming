#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first 'x' integers in 'my_list'
    without any separation, in the same line,
    then a new line.
    Any element in 'my_list' that's not an
    integer is skipped BUT STILL IS accounted for
    'x'.
    If no elements were printed, then no new line
    is printed either.
    """
    integers_printed = 0

    while integers_printed < x:
        try:
            print("{:d}".format(my_list[index]), end="")
        except IndexError:
            break
        except (ValueError, TypeError) as error:
            pass
        integers_printed += 1

    if integers_printed:
        # if nothing was printed,
        # a new line isn't allowed.
        print()
    return integers_printed
