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
    MATRIXERR = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or not
       all(isinstance(elem, list) for elem in matrix)):
        raise TypeError(MATRIXERR)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    buffer_list = []
    len_row = len(matrix[0])
    for elem in matrix:
        if len_row != len(elem):
            raise TypeError("Each row of the matrix must have the same size")
        for num in elem:
            if isinstance(num, (int, float)):
                buffer_list.append(round(num / div, 2))
            else:
                raise TypeError(MATRIXERR)
        new_matrix.append(buffer_list)
        buffer_list = []

    return new_matrix
