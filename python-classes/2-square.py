#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:27:00 2023.

@author: jgnacio
@description:

"""


class Square():
    """Represent a Square with size."""

    def __init__(self, size=0):
        """
        Initialize an empty Square.

        with a private instance attribute size
        """
        if isinstance(size, int):
            if size >= 0:
                self._Square__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
