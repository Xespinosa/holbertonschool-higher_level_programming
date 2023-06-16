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

    def __init__(self, size=0):
        """
        Initializes a new instance of Square with 'size' as an attribute.
        """

        if size < 0:
            raise ValueError("size must be >= 0")
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")

    def area(self):
        """
        define and return the area of a square
        """

        return (self.__size ** 2)
