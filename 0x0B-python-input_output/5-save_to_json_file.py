#!/usr/bin/python3
"""Writing to JSON file function definition"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text fileusing JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
