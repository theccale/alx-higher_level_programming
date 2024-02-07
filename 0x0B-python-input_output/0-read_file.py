#!/usr/bin/python3
""" to read a file """

def read_file(filename=""):
    """Print all the contents of a UTF8 text file to stdout."""
    with open(filename,encoding="utf-8") as me:
        print(me.read() , end="")

