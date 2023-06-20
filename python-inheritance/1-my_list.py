#!/usr/bin/python3
"""class MyList that inherits from list
"""


class Mylist(list):
    """Public instance method called Mylist
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
