#!/usr/bin/python3
"""
class rectangle
"""

from models.base import Base

class Rectangle(Base):
    """Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle"""
        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
