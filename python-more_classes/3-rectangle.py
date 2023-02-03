#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 14:09:00 2023.

@author: jgnacio
@classes:
    Rectangle:
        In this class is for representing an rectangle.

        methods:
            area - (nothing):
                this function returns the area of the rectangle

            perimeter - (nothing):
                this function returns the perimeter of the rectangle.
"""


class Rectangle:
    """Representation for Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializate the rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    def __str__(self):
        """Return a string representation of the Square."""
        if self.__width == 0 or self.__height == 0:
            return ""

        out_format = ""

        for i in range(self.__height):
            for j in range(self.__width):
                out_format += "#"
            out_format += "\n"

        return out_format[:-1]

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
