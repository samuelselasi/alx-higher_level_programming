#!/usr/bin/python3
"""1. Divide a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    Raise TypeError and ZeroDiviionError with messages
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    terr_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(terr_msg)

    _len = 0
    serr_msg = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(terr_msg)

        if _len != 0 and len(elems) != _len:
            raise TypeError(serr_msg)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(terr_msg)

        _len = len(elems)

    r = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (r)
