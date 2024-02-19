#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using earlier BaseGeometry"""
    def __init__(self, width, height):
        """Foe every new rectangle
        Args:
        width (int): The width of the new Rectangle.


        """
