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

    def area(self):
        """area """
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    square that inherits from Rectangle
    """
    def __init__(self, size):
        """self size init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """prints [Square] <width>/<height>"""
        return "[Square] {}/{}".format(self.__size, self.__size)
