#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:23:00 2023.

@author: jgnacio
"""


class Square():
    """Represent a Square with size."""

    def __init__(self, size=0):
        """
        Initialize an instance of Square.

        with a private instance attribute size
        """
        self._Square__size = size

    @property
    def size(self):
        """Return the size of the Square."""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if isinstance(value, int):
            if value >= 0:
                self._Square__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area of the Square."""
        return self._Square__size ** 2

    def my_print(self):
        """Print the size of the Square."""
        if self._Square__size == 0:
            print()
            return
        for i in range(self._Square__size):
            for j in range(self._Square__size):
                print("#", end="")
            print()
