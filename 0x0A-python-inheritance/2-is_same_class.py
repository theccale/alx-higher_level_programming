#!/usr/bin/python3
""" function that returns True if the object is exactly an instance of the specified class ; otherwise False."""

def is_same_class(obj, a_class):
    """ alwyas check if the object is exactly an instance of the specified class ; otherwise False.
    
    Args:
    obj (any): The object to check.
    a_class (type): the class to match the type of obj to.
    Returns:
    if obj is excatly an instance of a_class - True.
    otherwise - False


    """
if type(obj) == a_class:
    return True
return False

