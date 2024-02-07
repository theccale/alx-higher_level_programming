#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation."""
import json

def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON rep."""
    with open(filename, "w") as me:
        json.dump(my_oj, me)

        
