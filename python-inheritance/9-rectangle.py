#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 9 13:45:00 2023.

@author: jgnacio
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
