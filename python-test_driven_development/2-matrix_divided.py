#!/usr/bin/python3
"""
Created on Thu Jan 31 13:00:00 2023.

@author: jgnacio
@description:
This module have a function:
    matrix_divided (matrix, div) - that divide the matrix
"""

def matrix_divided(matrix, div):
    """Divides the matrix."""
    if (not isinstance(matrix, list)
        or not all(isinstance(elem, list) for elem in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = matrix[:]
    len_row = len(new_matrix[0])
    for i, elem in enumerate(new_matrix):
        if len_row != len(elem):
            raise TypeError("Each row of the matrix must have the same size")
        for j, num in enumerate(elem):
            if isinstance(num, (int, float)):
                new_matrix[i][j] = round(num / div, 2)
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return new_matrix
