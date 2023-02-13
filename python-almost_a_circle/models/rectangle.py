#!/usr/bin/python3
"""
Make a rectangle class that inherits from
the 'Base' class in 'base.py' in this folder,
with a width, a height, an x and a y
protected attribute.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class with a width, a height,
    an x and a y protected attribute.

    All of the attributes written in this class
    are supposed to be integers.
    Otherwise, TypeError is raised.

    'width' and 'height' are supposed to be
    positive, and 'x' and 'y' are supposed to be
    great or equal to 0; otherwise, ValueError
    is raised.
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        result = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        result += f" - {self.width}/{self.height}"
        return result

    def to_dictionary(self):
        """
        Returns the dictionary representation of all of
        self's public attributes (name: value)
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def update(self, *args, **kwargs):
        """
        Updates all of 'self's attributes like this:
        arg0 -> id
        arg1 -> width
        arg2 -> height
        arg3 -> x
        arg4 -> y
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for name, value in kwargs.items():
                self.__setattr__(name, value)

    def area(self):
        """
        Returns what the area of 'self' is,
        according to Euclidian Geometry and
        'self.__width' and 'self.__height'.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints a rectangle to the standard output
        using "#" as blocks, corresponding to
        'self.__width' and 'self.__height'.
        """
        print("\n" * self.y, end="")

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
