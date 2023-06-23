#!/usr/bin/python3

"""_summary_
"""


class Base:
    """_summary_
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            __nb_objects = + 1
            self.id = __nb_objects

    def integer_validator(self, name, value):
        """method that validates value"""

        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def integer_validator_var(self, name, value):
        """method that validates value for x and y"""

        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value < 0:
                raise ValueError(f"{name} must be >= 0")


