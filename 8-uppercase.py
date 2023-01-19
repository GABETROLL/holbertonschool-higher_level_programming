#!/usr/bin/python3
def uppercase(str):
    for c in str:
        output_char = c

        is_lowercase = ord(c) >= 97 and ord(c) <= 122
        if is_lowercase:
            output_char = chr(ord(c) - 32)
            # make uppercase

        print(output_char, end="")
