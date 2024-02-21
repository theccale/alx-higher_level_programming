#!/usr/bin/python3
"""a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""

def inherits_from(obj, a_class):
    """code hecks if an objcetis an inherited instance of a class

    Args:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj
    Returns;
    If obj is an inherited instance of a_class - True
    Otherwise _ False

    """
    if issubclass(type(obj), a_class) and type(obj) != a_class
            return True
        return False
