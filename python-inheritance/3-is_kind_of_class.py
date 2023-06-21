#!/usr/bin/python3
"""comment
"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise False

    Args:
        obj (any): object to be evaluated
        a_class (any): class to be evaluated

    Returns:
        boolean: True on Success, False otherwise
    """

    return isinstance(obj, a_class)
