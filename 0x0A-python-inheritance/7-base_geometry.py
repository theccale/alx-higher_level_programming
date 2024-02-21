#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)."""

class BaseGeometry:
        """Represents BaseGeometry"""
        def area(self):
            """ it is still an empty class"""
            raise Exception("area() is not implemented")
        def integer_validator(self, name, value):
            """validates a parameter receiveed as an interger
            Args:
                name (str): The name of the parameter .
                value (int): The parameter to validaet.
                Raises:
                TypeError: If value is not an interger.
                ValueError: If value is <= 0.

            """
            if type(value) !=int:
                raise TypeError("{}must be an integer".format(name)
                                if value <= 0
                                raise ValueError("{} must be greater than 0".format(name))
