#!/usr/bin/python3
"""This is a function that returns the list of available attributes and
methods of an object
"""


def lookup(obj):
    """This will return the available attributes and methods of a list
    object

    Args:
        obj (any): object given by the main

    Returns:
        list: a list of all the attributes and methods of the object
    """
    return dir(obj)
