#!/usr/bin/python3
"""1. Divide a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides the integer/float numbers of a matrix
    Raise TypeError if elements of matrix/div/list != int/float/matrix size !=
    Raise ZeroDivisionError if div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    errt_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(err_msg)

    elen = 0
    errs_msg = "Each row of the matrix must have the same size"

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(errs_msg)

        if elen != 0 and len(i) != elen:
            raise TypeError(errs_msg)

        for j in i:
            if not type(j) in (int, float):
                raise TypeError(errs_msg)

        elen = len(i)

    mtx = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (mtx)
