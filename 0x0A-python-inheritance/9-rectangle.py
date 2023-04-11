#!/usr/bin/python3
"""9. Full rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    (task based on 8-rectangle.py)
    """

    def __init__(self, width, height):
        """A function that initializes width and height"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Function that computes area of a rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """print() to print & str() to return: [Rectangle] <width>/<height>"""

        description = "[" + str(self.__class__.__name__) + "] "
        description += str(self.__width) + "/" + str(self.__height)
        return (description)
