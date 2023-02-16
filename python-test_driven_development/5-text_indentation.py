#!/usr/bin/python3
"""
Make a function that prints 2 new lines after
every ".", "?" or ":" in text, with the rest
of the content in that text.
"""


def text_indentation(text):
    """
    Prints all the contents of the 'text' string,
    but printing 2 new line characters instead of
    every ".", "?" or ":".

    If 'text' is not a string, TypeError is raised.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    result = text
    for punctuation in ".?:":
        result = result.replace(punctuation, "\n\n")

    print(result)
