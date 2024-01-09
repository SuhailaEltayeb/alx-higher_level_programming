#!/usr/bin/python3
"""JSON file-reading function definition"""
import json


def load_from_json_file(filename):
    """Creating Python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
