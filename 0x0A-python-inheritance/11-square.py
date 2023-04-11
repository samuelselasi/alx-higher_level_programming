#!/usr/bin/python3
"""11. Square #2"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """A function that initializes width and height"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Function that computes area of a square"""

        return (self.__size * self.__size)

    def __str__(self):
        """print() to print & str() to return: [Square] <width>/<height>"""

        description = "[" + str(self.__class__.__name__) + "] "
        description += str(self.__size) + "/" + str(self.__size)
        return (description)
