#!/usr/bin/python3
"""Module to compar an object to a class and ascertain if they are
    equivalent
    """


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly an instance of
    the specified class ; otherwise False

    Args:
        obj (any): object to be compared against a_class
        a_class (any): class to be compared against object

    Returns:
        Boolean: True on success, False otherwise
    """
    return type(obj) is a_class
