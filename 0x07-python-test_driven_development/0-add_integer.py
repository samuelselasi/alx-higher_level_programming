#!/usr/bin/python3
"""0. Integers addition"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    Raise TypeError if a or b are not integers/floating points
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
