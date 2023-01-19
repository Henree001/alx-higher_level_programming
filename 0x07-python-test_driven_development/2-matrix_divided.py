#!/usr/bin/python3
"""Defines a function that divides all element of a matrix"""


def matrix_divided(matrix, div):
    """Divides all element of matrix by div.
    Args:
        matrix(list): A list of lists of ints or floats.
        div(int/float): the divisor
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
        """

    text = 'matrix must be a matrix (list of lists) of integers/floats'
    for item in matrix:
        for i in item:
            if type(i) != int and type(i) != float:
                raise TypeError(text)
        if len(item) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for item in matrix:
        row = []
        for i in item:
            row.append(round(i / div, 2))
        new_matrix.append(row)
    return new_matrix
