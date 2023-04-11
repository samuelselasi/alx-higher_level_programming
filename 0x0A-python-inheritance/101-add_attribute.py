#!/usr/bin/python3
"""13. Can I?"""


def add_attribute(obj, att, value):
    """A function that adds a new attribute to an object if it’s possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
