#!/usr/bin/python3
"""
This module creates and manipulates a square
"""


class square:
    """
    create the square
    """

    def __init__(self, size=0):
        """define the size of the square
        """

        if size < 0:
            raise ValueError("size must be >= 0")
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
