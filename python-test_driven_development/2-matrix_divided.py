#!/usr/bin/python3
"""Holberton School."""


def matrix_divided(matrix, div):
    """Divides a matrix."""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    # print(type(matrix))
    if not type(matrix) == list:
        raise TypeError(err)
    if type(div) != int:
        raise TypeError("div must be a number")
    if len(matrix) > len(matrix) + 1:
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
        """
        for i in matrix:
            for j in i:
                print(type(matrix))
                new_matrix.insert(j, j / div)
        """
    return new_matrix
