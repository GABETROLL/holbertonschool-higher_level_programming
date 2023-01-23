#!/usr/bin/python3


def no_c(my_string):
    # for-loop generator expression, but with an if statement
    # that skips the item if the condition here
    # doesn't come true                 \/\/\/\/\/\/\/\/\/\/\/\/
    return "".join(c for c in my_string if c != "c" and c != "C")
