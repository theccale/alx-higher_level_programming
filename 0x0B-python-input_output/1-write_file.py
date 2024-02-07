#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and returns the number of characters written"""

def write_file(filename="", text=""):
    """a string to a text file (UTF8)

    Args:
    filename (str):   the file name
    text (str): what text to write to file
    Returns: The total number of character written."""
    with open(filename, "w", encoding="utf-8") as me;
    return me.write(text)

