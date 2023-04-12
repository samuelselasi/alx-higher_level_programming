#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """A class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """A function that initiates public instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A function that returns dictionary representation of Student"""

        return (self.__dict__)
