#!/usr/bin/python3
""" function that adds a new attribute to an object if it’s possible:"""
def add_attribute(obj, att, value):
    """adds a new attribute to an object if it’s possible:

    Args:
    obj (any): The object to add a new attribute to.
    att (str): The name of the attribute to add to obj
    value (any): The value pf att
    Raises:
    TypeError: If the attribute cannot be added.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
        setattr(obj, att, value)
