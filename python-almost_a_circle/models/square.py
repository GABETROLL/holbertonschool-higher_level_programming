#!/usr/bin/python3
"""
Make a square class that inherits from 'Rectangle'.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Functions the same way as 'Rectangle',
    but the width and height correspond the
    'size' parameter and property.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        the length of each side of 'self'
        """
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be >= 0")

        self.__width = value
        self.__height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
