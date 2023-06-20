#!/usr/bin/python3
"""class MyList that inherits from list
"""


class Mylist(list):
    """Public instance method

    Args:
        list (list): list of elements type int
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
