#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:24:00 2023.

@author: jgnacio
@description:

"""

from models import Base


class Rectangle(Base):
    """Representation of a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Return the x coordinate of the rectangle."""
        return self.__x

    @property
    def y(self):
        """Return the x coordinate of the rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the widht of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x position of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the y position of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height