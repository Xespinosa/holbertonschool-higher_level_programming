#!/usr/bin/python3
"""This module creates and manipulates a square"""


class square:
    """create the square"""

    def __init__(self, size=0):
        """define the size of the square"""
        self.size = size

    def size(self, value):
        """size setter"""
        if value < 0:
            raise ValueError("size must be >= 0")
        try:
            self.__size = value
        except TypeError:
            print("size must be an integer")

    def size(self):
        """size getter"""
        return self.__size

    def area(self):
        """define and return the area of a square"""
        return (self.__size ** 2)
