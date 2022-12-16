#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squarevalue = [[row[j]**2 for j in range(len(row))] for row in matrix]
    return squarevalue
