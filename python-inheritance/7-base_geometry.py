#!/usr/bin/python3
"""area(self)"""


class BaseGeometry:
    """area(self)"""

    def area(self):
        """area(self)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
