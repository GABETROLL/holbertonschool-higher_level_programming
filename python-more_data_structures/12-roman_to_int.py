#!/usr/bin/python3


def roman_to_int(roman_string):
    """
    Returns the integer corresponding
    to the roman numeral 'roman_string'

    The 'roman_string' MUST be a string
    and be a value in the range [1, 3999]
    """
    if type(roman_string) != str:
        return 0

    DIGIT_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000}
    # constants are defined UPPER_CASE
    result = 0

    last_roman_digit = ""
    for roman_digit in reversed(roman_string):
        value = DIGIT_VALUES[roman_digit]

        if last_roman_digit:
            last_value = DIGIT_VALUES[last_roman_digit]

            if value < last_value:
                result -= value
                continue

        result += value
        last_roman_digit = roman_digit

    return result
