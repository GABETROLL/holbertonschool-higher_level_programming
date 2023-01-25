#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints the key-value pairs in the dict 'a_dictionary'
    like this: "{key}: {value}"
    BUT with the pairs being sorted by the keys
    """
    # 'a_dictionary.items()' returns a collection of tuples
    # with each key-value pair in 'a_dictionary' like this: (key value)
    for key, value in sorted(a_dictionary.items(), key=lambda pair: pair[0]):
        print(f"{key}: {value}")
