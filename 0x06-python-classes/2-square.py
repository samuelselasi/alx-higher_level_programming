#!/usr/bin/python3
"""
2. Size validation
A class Square that defines a square
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """
        Define private instance attribute: size
        Raise TypeError & ValueError if not int or <0 resp.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
