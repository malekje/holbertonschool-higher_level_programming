#!/usr/bin/python3
"""
Rectangle class

"""


class Rectangle:
    """
    Rectangle class

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        """
        rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        hight setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimetre
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        print the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i != self.__height - 1:
                rectangle += ("\n")
        return (rectangle)

    def __repr__(self):
        """
        representing the rectangle
        """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        """
        instance deletion
        """
        print("Bye rectangle...")
