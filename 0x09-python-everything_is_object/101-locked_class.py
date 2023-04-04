#!/usr/bin/python3
"""30. Low memory cost"""


class LockedClass:
    """Class to prevent user from dynamically creating new instances"""

    __slots__ = ['first_name']
