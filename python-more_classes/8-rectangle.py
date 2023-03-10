#!/usr/bin/python3
"""
Exercise 8: Copy 'Rectangle' class from
exercise 7 and make a static method that
returns the rectangle with the bigger area.
"""


class Rectangle:
    """
    The width and height are properties with
    getters and setters.

    To set an attribute, it must be a positive
    integer.

    'Rectangle.number_of_instances' indicates
    how much instances of 'Rectangle' are
    alive at run-time. It gets incremented
    when making the instance and when deleting
    or "losing" the object.

    Its string representation is printed using
    the string representation of the 'print_symbol'
    class variable.

    Deleting the instance will print out
    "Bye rectangle..." (so sad)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = None
        self.__height = None

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the rectangle with the bigger
        area. If they both have the same area,
        this method returns 'rect_1'.
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

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
        rectangle string made with copies of
        'Rectangle.print_symbol' and new
        lines.
        """
        if not self.width or not self.height:
            return ""
        line = str(self.print_symbol) * self.width
        return "\n".join(line for _ in range(self.height))

    def __repr__(self):
        """
        Returns the syntax to construct 'self'
        with 'eval'.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints "Bye rectangle..." when 'self'
        gets deleted or is "collected as garbage",
        then decrements 'Rectangle.number_of_instances'
        to indicate that one less 'Rectangle' exists.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
