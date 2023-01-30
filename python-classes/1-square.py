#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:46:00 2023.

@author: jgnacio
@description:

"""


class Square():
    """Represent a Square with size."""

    __size = 0

    def __init__(self, size):
        """
        Initialize an empty Square.

        with a private instance attribute size
        """
        Square.__size = size
        self._Square__size = Square.__size
