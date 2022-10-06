#!/usr/bin/python3
""" class square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        """size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Prints Square"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """assigns attributes"""

        if args and len(args) != 0:
            for index in range(len(args)):
                if index == 0:
                    self.id = args[index]
                elif index == 1:
                    self.size = args[index]
                elif index == 2:
                    self.x = args[index]
                elif index == 3:
                    self.y = args[index]
        else:
            if len(kwargs) > 0:
                key = kwargs.keys()
                for i in key:
                    if i == 'id':
                        self.id = kwargs['id']
                    elif i == 'size':
                        self.size = kwargs['size']
                    elif i == 'x':
                        self.x = kwargs['x']
                    elif i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """dictionaryof a rectangle"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y}
