#!/usr/bin/python3
"""
9. Compare 2 squares
A class Square that defines a square
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Define private instance attribute: size"""

        self.__size = size

    @property
    def size(self):
        """"Function that returns private instance attribute: size"""

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

        return self.__size ** 2

    def __le__(self, other):
        """Function that compares if a sqare is <= another"""

        return self.area() <= other.area()

    def __lt__(self, other):
        """Function that compares if a square is < another"""

        return self.area() < other.area()

    def __ge__(self, other):
        """Function that compares if a square is >= another"""

        return self.area() >= other.area()

    def __ne__(self, other):
        """Function that compares if a square is != another"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Function that compares if a square is > another"""

        return self.area() > other.area()

    def __eq__(self, other):
        """Function that compares f a square == another"""

        return self.area() == other.area()
