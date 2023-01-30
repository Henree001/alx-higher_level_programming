#!/usr/bin/python3
"""Defines a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the Square class"""
    def __init__(self, size):
        """Initialize a new Square
        Args:
            size(int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
