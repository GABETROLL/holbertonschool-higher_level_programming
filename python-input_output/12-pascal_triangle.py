#!/usr/bin/python3
"""
Exercise 12: Interview preparation

Write a function that returns a list of lists
representing the first n rows of the pascal triangle,
starting from row 0, like this:
pascal_trinangle(5) ->
[
    [1],              # 0
    [1, 1],           # 1
    [1, 2, 1],        # 2
    [1, 3, 3, 1],     # 3
    [1, 4, 6, 4, 1]   # 4
]"""


def pascal_triangle(n):
    """
    Returns a list of lists representing
    the first 'n' rows of the pascal triangle
    (from index 0 to n - 1), where 'n' is
    the parameter right above this sentence.

    If n < 0, the result of this function is
    an empty list.

    ALWAYS ASSUMES 'n' IS AN INTEGER.
    """
    if n <= 0:
        return []

    result = [[1]]
    for _ in range(n - 1):
        last_row = [0] + result[-1] + [0]
        next_row = []
        for m_index in range(len(last_row) - 1):
            next_row.append(last_row[m_index] + last_row[m_index + 1])
        result.append(next_row)
    return result
