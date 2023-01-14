#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the current size of the square."""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
