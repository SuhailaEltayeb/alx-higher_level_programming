#!/usr/bin/python3
"""Function returns an object from JSON string."""
import json


def from_json_string(my_str):
    """Returns object Rep. of JSON string"""
    return json.loads(my_str)
