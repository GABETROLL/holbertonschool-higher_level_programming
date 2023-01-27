#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first 'x' integers in 'my_list'.
    Any element in 'my_list' that's not an
    integer is skipped and isn't accounted for
    'x'.
    """
    integers_printed = 0

    for index in range(x):
        try:
            print("{:d}".format(my_list[index]))
        except IndexError:
            break
        except (ValueError, TypeError) as error:
            continue
        # if the index is out of range,
        # the printing is over, so, we have to break.
        # Unlike the type being wrong, which we just have to
        # not count it as printed.
        # the code below runs if it was fully successful.
        integers_printed += 1
    return integers_printed
