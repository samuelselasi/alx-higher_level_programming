#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """A class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """A function that initiates public instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A function that returns dictionary representation of Student"""

        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return ({j: getattr(self, j) for j in attrs if hasattr(self, j)})

        return (self.__dict__)
