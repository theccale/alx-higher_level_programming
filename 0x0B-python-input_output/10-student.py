#!/usr/bin/python3
""" a function that defines  class Student that defines a student by: (based on 9-student.py)"""

class Student:
    """ To represent each student"""
    def __init__(self, first_name, last_name, age):
"""For every new student;
    Args;
    first_name (str) :
    The first name of the student
    last_name (str) :
    The last name of the student
    age (int) :The student's age.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self,attrs=None):
        """For the idctionary representation of each student 
        if attrs is a list of strings, represents only those attributes included in the list.
        Args:
            attrs (list) the attributes to represent."""
            if (type(attrs) == list and 
                all(type(ele) == str for ele in attrs)):
                return {k:getattr(self, k) for k in attrs if hasattr(self,k)}
                return self.__dict__
            
