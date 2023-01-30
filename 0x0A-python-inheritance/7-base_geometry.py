#!/usr/bin/python3
"""
Defines the class BaseGeometry
"""


class BaseGeometry:
    """Represents a BaseGeometry class"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name: string
            value: argument to be validated
        Raises:
              TypeError: if value is not an integer
              ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
