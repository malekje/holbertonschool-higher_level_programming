#!/usr/bin/python3
"""
class rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def x(self):
        """x"""
        return self.__x

    @property
    def y(self):
        """y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """getting area"""
        return self.__width * self.__height

    def display(self):
        """stdout rectangle"""
        for l in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width + self.__x):
                if j < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update"""
        if args and len(args) != 0:
            for index in range(len(args)):
                if index == 0:
                    self.id = args[index]
                elif index == 1:
                    self.__width = args[index]
                elif index == 2:
                    self.__height = args[index]
                elif index == 3:
                    self.__x = args[index]
                elif index == 4:
                    self.__y = args[index]
        else:
            if len(kwargs) > 0:
                key = kwargs.keys()
                for i in key:
                    if i == 'id':
                        self.id = kwargs['id']
                    elif i == 'width':
                        self.__width = kwargs['width']

                    elif i == 'height':
                        self.__height = kwargs['height']
                    elif i == 'x':
                        self.__x = kwargs['x']
                    elif i == 'y':
                        self.__y = kwargs['y']

    def to_dictionary(self):
        """return the dictionary of a rectangle"""

        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width}
