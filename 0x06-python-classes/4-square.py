#!/usr/bin/python3
"""
4. Access and update private attribute
A class Square that defines a square
"""


class Square:
    """A class that defines a square"""

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

    @property
    def size(self):
        """Function that returns size"""

        return self.__size

    @size.setter
    def size(self, value):
        """
        Define private instance attribute: value
        Raise TypeError & ValueError if not int or <0 resp.
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Function that calculates area"""

        return (self.__size ** 2)
