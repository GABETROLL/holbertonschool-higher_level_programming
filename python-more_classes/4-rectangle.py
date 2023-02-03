#!/usr/bin/python3
"""
Exercise 4: Copy 'Rectangle' class from
exercise 3 and add its string '__repr__'
to be able to use it with 'eval' for making
a new instance at run-time
"""


class Rectangle:
    """
    The width and height are properties with
    getters and setters.

    To set an attribute, it must be a positive
    integer.

    Its string representation is made-up of
    "#"'s.

    Its '__repr__' can be used with 'eval'
    to create a copy of itself at run-time.
    """
    def __init__(self, width=0, height=0):
        self.__width = None
        self.__height = None

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns this recangle's area according
        to euclidian geometry, based in
        'self.__width' and 'self.__height'.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns this recangle's perimeter
        according to euclidian geometry, based
        in 'self.__width' and 'self.__height'.

        If 'self.__width' or 'self.__height' are
        0, this function returns 0.
        """
        if not self.__width or not self.__height:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Returns a 'self.width' * 'self.height'
        rectangle string made with "#"'s and new
        lines.
        """
        if not self.width or not self.height:
            return ""
        line = "#" * self.width
        return "\n".join(line for _ in range(self.height))
    
    def __repr__(self):
        """
        Returns the syntax to construct 'self'
        with 'eval'.
        """
        return f"Rectangle({self.width}, {self.height})"
