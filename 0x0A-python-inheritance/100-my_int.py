#!/usr/bin/python3
"""12. My integer"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, value):
        """Function that inverts == operation"""

        return (self.real != value)

    def __ne__(self, value):
        """Function that inverts != operation"""

        return (self.real == value)
