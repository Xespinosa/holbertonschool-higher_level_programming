#!/usr/bin/python3
from models.base import Base
"""module for rectangle
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
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
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    def get_height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    def get_x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    def get_y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__y

    def set_width(self, width):
        """_summary_

        Args:
            width (_type_): _description_
        """
        self.__width = width

    def set_height(self, height):
        """_summary_

        Args:
            height (_type_): _description_
        """
        self.__height = height

    def set_x(self, x):
        """_summary_

        Args:
            x (_type_): _description_
        """
        self.__x = x

    def set_y(self, y):
        """_summary_

        Args:
            y (_type_): _description_
        """
        self.__y = y

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width * self.__height

    def display(self):
        """_summary_
        """
        for i in range(self.__y):
            print()
            for i in range(self.__width):
                for j in range(self.__x):
                    print(" ", end="")
                for j in range(self.__height):
                    print('#', end='')
                print()

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        id_str = str(self.id)
        x_str = str(self.__x)
        y_str = str(self.__y)
        width_str = str(self.__width)
        height_str = str(self.__height)

        rectangle_str = "[Rectangle] (" + id_str + ") " + x_str + \
            "/" + y_str + " - " + width_str + "/" + height_str
        return rectangle_str

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute

        Args:
            *args (ints): values to assign to id, width, height, x, y (in that
              order) **kwargs: dictionary of attributes and their values
              to assign
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to return the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}
