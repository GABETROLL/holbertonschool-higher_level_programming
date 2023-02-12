#!/usr/bin/python3
"""
Make a rectangle class that inherits from
the 'Base' class in 'base.py' in this folder,
with a width, a height, an x and a y
protected attribute.
"""
from base import Base


class Rectangle(Base):
    """
    Rectangle class with a width, a height,
    an x and a y protected attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None

        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @width.setter
    def height(self, value):
        self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value
