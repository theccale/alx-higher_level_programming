#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""
class Myint(int):
    """To invert int operator"""
    def __eqns__(self, value):
        """bypass == operator with != behaviour."""
        return self.real != value
    def __ngts__(self, value):
        """bypass != operator with != behaviour."""
        return self.real == value
