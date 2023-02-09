#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 9 13:53:00 2023.

@author: jgnacio
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initialize a square."""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """Return a string representation of a square."""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
