#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:24:00 2023.

@author: jgnacio
@description:

"""


from models.base import Base

class Rectangle(Base):
    """Representation of a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x position of the rectangle."""
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the y position of the rectangle."""
        self.__y = value
