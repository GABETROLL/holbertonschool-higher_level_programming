#!/usr/bin/python3
def uppercase(str):
    for c in str:
        not_lowercase_output_char = c

        is_lowercase = ord(c) >= 97 and ord(c) <= 122
        if is_lowercase:
            not_lowercase_output_char = chr(ord(c) - 32)

        print("{}".format(not_lowercase_output_char), end="")
    print()
