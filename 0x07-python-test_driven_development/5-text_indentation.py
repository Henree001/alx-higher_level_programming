#!/usr/bin/python3
"""Defines a function that prints a string."""


def text_indentation(text):
    """Prints a string.
    Args:
        text: string to be printed.
    Raises:
        TypeError: if text is not a string.
    """
    idx = 0
    if type(text) != str:
        raise TypeError('text must be a string')
    for i in text:
        print(i, end='')
        if i == '.' or i == '?' or i == ':':
            print('\n')
            if text[idx + 1] == " ":
                continue
        idx += 1
