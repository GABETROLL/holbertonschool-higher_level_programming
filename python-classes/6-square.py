#!/usr/bin/python3
"""
How to customize a class' string representation
(and therefore how it's printed)
"""


class Square:
    """
    'Square' class that has all of its
    (theoretical) sides' lenghts as a 'size'
    private attribute with its getters and
    setters, and a 'position' private
    attribute, which determines how far away
    from the left and top the square gets printed
    when calling 'self.my_print()'.

    'size' MUST be an integer and MUST NOT be
    negative.

    'position' MUST be a tuple of two positive
    integers, or zeros.

    Its string representation is a square of '#'
    characters with width and height of 'self.size',
    which is found in 'my_print'.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = None
        self.size = size
        self.__position = None
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or \
        len(value) != 2 or \
        type(value[0]) != int or \
                type(value[1]) != int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        returns the area of the square
        (aka: 'self')
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints 'self' as a square of "#"
        with sides of length 'self.size',

        with 'self.position[1]' new lines of
        vertical padding and 'self.position[0]'
        spaces of left padding before the "#"'s.
        """
        print("\n" * self.positioj[1], end="")
        print(*(" " * self.position[0] + \
                "#" * self.size for _ in range(self.size)), sep="\n")
