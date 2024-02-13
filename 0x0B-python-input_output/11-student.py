#!/usr/bin/python3
""" A function that that defines a student by: (based on 10-student.py) """

class Student:
    """the details of the student"""

    def __init__(self, first_name, last_name, age):
        """To start with a new student.
            
            Args:
                first_name (str): The first name of the student.
                 last_name (str): The last name of the student.
                age (int): The student's age.

        """
        self.first_name = first_name
         self.last_name = last_name
         self.age = age
         def to_json(self, attrs=None):
             """A dictionary representation of each student.
                 If attrs is a list of strings, represents only those attributes included 
                 Args:
                    atts (list): what attributes to rep

             """
             if (type(attrs) == list 
                 and
                 all(type(ele) == str for ele in attrs)):
                        return {k:getattr(self, k) for k in attrs
                                if hasattr(self, k)}
                        return self.__dict__

                    def reload_from_json(self, json):
                        """Now replace all the previous attribute of student.

                        Args:
                        json (dict): The key or value pairs to replace attributes with """
                        for k, v in json.items():
                            setattr(self, k, v)



