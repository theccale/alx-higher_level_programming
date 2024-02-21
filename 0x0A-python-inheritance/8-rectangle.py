#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """ For every new rectangle
        Args:
        width (int); The width of the rrectangle
        height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
            self.__width = width
        self.integer_validator("height", height)
            self.__height = height
