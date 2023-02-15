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
        # Not mandatory
        # if not isinstance(value, int):
        #     raise TypeError("size must be an integer")
        # if value <= 0:
        #     raise ValueError("size must be > 0")
        self.width = value
        self.height = value
