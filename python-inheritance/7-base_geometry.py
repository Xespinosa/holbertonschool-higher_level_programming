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
        """validates that the value given is an integer

        Args:
            name (string): name of the value given
            value (int): value being validated
        """
        if type(value) is not int:
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')
