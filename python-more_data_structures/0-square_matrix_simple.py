#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        square = []
        for y in x:
            square.append(y*y)
        new_matrix.append(square)
    return new_matrix
