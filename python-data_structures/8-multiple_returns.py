#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple with the length of the sentence and
    its first character, if it's not "" or None,
    otherwise (0, None)
    """
    # the parenthesi are redundant
    if sentence and len(sentence):
        return len(sentence), sentence[0]
    return 0, None
