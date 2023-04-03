#!/usr/bin/python3
"""1. Real definition of a rectangle"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Function that initializes instances for width & height"""

        self.height = height
        self.width = width

    @property
    def height(self):
        """Function that retrieves height instance attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """
        function that sets height instance attribute
        Raise TypeError and ValueError if not integer or natural number resp.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """Function that retrieves width instance attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        Function that sets width instance attribute
        Raise TypeError & ValueError if not integer or natural number resp.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
