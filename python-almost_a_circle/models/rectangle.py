#!/usr/bin/python3
from models.base import Base
"""
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        super().integer_validator_var('x', x)
        super().integer_validator_var('y', y)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y
    
    def area(self):
        return self.__width * self.__height 
