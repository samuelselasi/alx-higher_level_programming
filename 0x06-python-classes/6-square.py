#!/usr/bin/python3
"""
6. Coordinates of a square
A class Square that defines a square
"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Define private instance attributes: size & position"""

        self.size = size
        self.position = position

    def __str__(self):
        """Define private instance attribute: my_print"""

        self.my_print()

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

    @property
    def position(self):
        """Define private instance attribute: position"""

        return self.__position

    @position.setter
    def position(self, value):
        """
        Function that sets position of the square
        Raise TypeError if value is not tuple or value !=2 or <0
        """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')

        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Function that calculates area"""

        return self.__size ** 2

    def pos_print(self):
        """Function that returns position in space"""

        s_position = ""
        if self.size == 0:
            return "\n"

        for n in range(self.position[1]):
            s_position += "\n"

        for n in range(self.size):
            for x in range(self.position[0]):
                s_position += " "

            for y in range(self.size):
                s_position += "#"

            s_position += "\n"

        return s_position

    def my_print(self):
        """Function that prints square with the '#' character"""

        print(self.pos_print(), end='')
