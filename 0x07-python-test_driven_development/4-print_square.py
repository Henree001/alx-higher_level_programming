#!/usr/bin/python3
"""Defines a function that prints a square."""


def print_square(size):
    """Prints a square.
    Args:
        size: size of the square of type int.
    Raise:
        TypeError: if size is not an integer.
        ValueError: if size is less than zero.
        TypeError: if size is a float and less than 0.
    """

    if type(size) = float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
