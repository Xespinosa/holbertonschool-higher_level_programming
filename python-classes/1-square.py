#!/usr/bin/python3
"""
This module defines a class 'Square'.
"""


class square:
    """
    A class that defines a square with a private instance attribute 'size',
    and methods for getting and setting the 'size' value, and for calculating
    the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of Square with 'size' as an attribute.
        """

        self.__size = size
