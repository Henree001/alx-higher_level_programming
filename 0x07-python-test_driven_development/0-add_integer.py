#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    Float arguments are typecasted into integers before addition is performed.

    Raises:
        TypeError: if either a or b is a non_integer or non-float.
    """

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError('a must be an integer')
    if type(b) != int:
        raise TypeError('b must be an integer')
    else:
        return a + b
