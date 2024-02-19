#!/usr/bin/python3

"""Write a class MyList that inherits from list"""

class MyLists(list):
    """prints he list, but sorted (ascending sort)"""

    def print_sorted(self):
        """to print a list in ascending order"""
        print(sorted(self))

