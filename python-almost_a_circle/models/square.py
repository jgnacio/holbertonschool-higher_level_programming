#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:41:00 2023.

@author: jgnacio
@description:

"""

from models import Rectangle


class Square(Rectangle):
    """Representation of a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/"\
               f"{self.y} - {self.width}"

    @property
    def size(self):
        """Return the width of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update arguments of the rectangle."""
        attrNames = ('id', 'size', 'x', 'y')

        if args:
            for key, value in zip(attrNames, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        attr_names = ("id", "x", "size", "y")
        my_dic = dict()
        for key in attr_names:
            my_dic[key] = getattr(self, key)

        return my_dic
