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
    
class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
