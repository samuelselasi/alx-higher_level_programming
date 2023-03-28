#!/usr/bin/python3
"""
10. ByteCode -> Python #5
"""
import math


class MagicClass:
    """Class that defines a circle"""

    def __init__(self, radius=0):
        """
        Define private instance attribute: radius
        Raise TypeError if radius is not an integer
        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Function that calculates area of a circle"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Function that calculates circumference of a circle"""

        return 2 * math.pi * self.__radius
