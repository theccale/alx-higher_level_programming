#!/usr/bin/python3
"""Function that creates an Object from a “JSON file”."""
import json


def
load_from_json_file(filename):
    """Create an Object from a JSON file."""
    with open(filename) as me:
              return json.load(me)

