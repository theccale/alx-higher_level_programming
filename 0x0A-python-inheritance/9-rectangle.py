#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using earlier BaseGeometry"""
    def __init__(self, width, height):
        """Foe every new rectangle
        Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.

        """
super().integer_validator("height", height)
        self.__height = height
super().integer_validator("width", width)
        self.__width = width
        def area(self):
            """return the area of the rectangle based on the width and height received"""
            return self.__width * self.__height

        def __str__(self):
            """ REturn the details of the new rectangle"""
            string = "[" + str(self.__class__.__name__) + "] "
            string += str(self.__width) + "/" + str (self.__height)
            return string
