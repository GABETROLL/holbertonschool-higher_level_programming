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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """
        If there are no 'args' present,
        they are skipped, and the 'kwargs'
        are used to set 'self's attributes.

        Otherwise, this method updates all
        of 'self's attributes like this:
        args[0] -> id
        args[1] -> size
        args[2] -> x
        args[3] -> y
        and skips 'kwargs' instead.
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                # all the args may not be there
                pass
        else:
            for name, value in kwargs.items():
                self.__setattr__(name, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
