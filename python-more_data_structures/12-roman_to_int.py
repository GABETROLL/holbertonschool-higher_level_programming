#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    Returns the integer corresponding
    to the roman numeral 'roman_string'

    The 'roman_string' MUST be a string
    and be a value in the range [1, 3999]
    """
    if type(roman_string) != str:
        return None

    digit_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result: int = 0

    last_roman_digit = ""
    for roman_digit in reversed(roman_string):
        if last_roman_digit and roman_digit < last_roman_digit:
            result -= digit_values[roman_digit]
        else:
            result += digit_values[roman_digit]
        last_roman_digit = roman_digit

    return result
