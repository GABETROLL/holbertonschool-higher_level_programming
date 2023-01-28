#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
        # most likely to fail at the function calling part
        # or the unpacking of the args.
    except Exception as error:
        # keyboard-interrupts (aka pressing Ctrl+C to
        # end a program that's still running)
        # is an exception that can be handled by Python.
        # We don't want to handle it, so we just write
        # 'Exception' instead, which is a class independant
        # of KeyboardInterrupt.
        print(f"Exception: {error}", file=stderr)
