#!/usr/bin/python3
def print_last_digit(number):
    # This time, we don't care about the sign ;)
    # (but Python does)
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
