#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:32:00 2023.

@author: jgnacio
"""


class Square():
    """Represent a Square with size."""

    TUPLEERROR = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize an instance of Square.

        with a private instance attribute size
        """
        self._Square__size = size
        if isinstance(position, tuple):
            try:
                if (isinstance(position[0], int) and
                   isinstance(position[1], int)):
                    if position[0] >= 0 and position[1] >= 0:
                        self._Square__position = position
                    else:
                        raise ValueError(Square.TUPLEERROR)
            except IndexError:
                raise IndexError(Square.TUPLEERROR)
        else:
            raise TypeError(Square.TUPLEERROR)

    @property
    def size(self):
        """Return the size of the Square."""
        return self._Square__size

    @property
    def position(self):
        """Return the position of the Square."""
        return self._Square__position

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

    @position.setter
    def position(self, value):
        """Set the position of the Square."""
        if isinstance(value, tuple):
            try:
                if (isinstance(value[0], int) and
                   isinstance(value[1], int)):
                    if value[0] >= 0 and value[1] >= 0:
                        self._Square__position = value
                    else:
                        raise ValueError(Square.TUPLEERROR)
            except IndexError:
                raise IndexError(Square.TUPLEERROR)
        else:
            raise TypeError(Square.TUPLEERROR)

    def area(self):
        """Return the area of the Square."""
        return self._Square__size ** 2

    def my_print(self):
        """Print the size of the Square."""
        if self._Square__size == 0:
            print()
            return

        for y in range(self._Square__position[1]):
            print()

        for i in range(self._Square__size):
            for x in range(self._Square__position[0]):
                print(" ", end="")
            for j in range(self._Square__size):
                print("#", end="")
            print()
