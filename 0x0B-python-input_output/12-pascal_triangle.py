#!/usr/bin/python3
"""Defines a function that returns a list of Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n: pascal triangle of integer(n)
    """
    if n <= 0:
        return (empty = [])
    pascal_list = [[1], [1, 1]]
    for i in range(n):
        temp = []
        for y in range(i + 1):
            temp[0 + x] + temp[1 + x]
            x += 1

