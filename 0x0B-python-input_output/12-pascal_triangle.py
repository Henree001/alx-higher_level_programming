#!/usr/bin/python3
"""Defines a function that returns a list of Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n: pascal triangle of integer(n)
    """
    if n <= 0:
        return []
    num = 1
    pascal_list = []
    for i in range(n):
        temp = []
        for y in range(i + 1):
            if i == 0 or i == y or y == 0:
                temp.append(num)
            else:
                temp.append(pascal_list[i - 1][y - 1] + pascal_list[i - 1][y])
        pascal_list.append(temp)
    return pascal_list
