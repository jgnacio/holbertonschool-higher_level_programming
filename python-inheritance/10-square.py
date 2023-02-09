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
        """initialize a square."""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """return the area of the square."""
        return self.__size ** 2
