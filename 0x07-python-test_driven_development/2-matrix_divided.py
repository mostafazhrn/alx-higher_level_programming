#!/usr/bin/python3
"""
This module divides a matrix by a number
Raises:
TypeErrors and ZeroDivisionErrors
"""


def matrix_divided(matrix, div):
    """Divides a matrix by a number
    Args:
        matrix (list): list of lists of integers or floats
        div (int/float): number to divide matrix
    Returns:
        new matrix
    """
    Error_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    Error_size = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(Error_matrix)
    taile = -1
    for row in matrix:
        if type(row) is not list:
            raise TypeError(Error_matrix)
        if taile == -1:
            taile = len(row)
        elif taile != len(row):
            raise TypeError(Error_size)
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(Error_matrix)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
