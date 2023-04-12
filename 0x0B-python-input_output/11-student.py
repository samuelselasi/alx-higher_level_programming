#!/usr/bin/python3
"""11. Student to disk and reload"""


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

    def reload_from_json(self, json):
        """A function that replaces all attributes of the Student instance"""

        for i, j in json.items():
            setattr(self, i, j)
