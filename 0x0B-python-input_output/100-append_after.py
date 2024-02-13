#!/usr/bin/python3

"""
a function that inserts a line of text to a file
"""
def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file, after each line containing a specific string
        Args:
        filename(str): The name of the file
        search_string (str): The string to search for within the file
        new_string (str): The new string to insert
    """
        text = ""
        with open(filename) as t:
            for line in t:
                text += line
                if search_string in line:
                    text += new_string
                    with open(filename, "ver") as
                    ver:
                        ver.write(text)


