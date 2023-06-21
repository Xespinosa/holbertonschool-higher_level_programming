#!/usr/bin/python3
"""module for a class called Base Geometry with public instance methods
"""


class BaseGeometry:
    """class with exceptions
    """
    def area(self):
        """defines the area of the geometry

        Raises:
            Exception: error message for user
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method that validates value"""

        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry

    Args:
        BaseGeometry (class): parent class
    """

    def __init__(self, width, height):
        """initialization method

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """area of the rectangle

        Returns:
            int: total area of the rectangle
        """

        return self._height * self._width

    def __str__(self) -> str:
        """string to print the width and height of the rectangle

        Returns:
            str: the height and width of the rectangle
        """

        return f"[Rectangle] {self._width}/{self._height}"


class Square(Rectangle):
    """a class Square that inherits from Rectangle

    Args:
        Rectangle (class): parent class for square
    """

    def __init__(self, size):
        """initialization of size

        Args:
            size (int): size of one of the sides of the square
        """

        super().integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        """area of the square

        Returns:
            int: integer value of the area
        """

        return self._size ** 2
