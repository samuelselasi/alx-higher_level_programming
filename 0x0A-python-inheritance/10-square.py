#!/usr/bin/python3
"""10. Square #1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """A function that initializes width and height"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
