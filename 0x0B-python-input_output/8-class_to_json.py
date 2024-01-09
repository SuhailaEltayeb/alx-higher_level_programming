#!/usr/bin/python3
"""Python class-to-JSON function definition"""


def class_to_json(obj):
    """Return simple data structure dictionary description ."""
    return obj.__dict__
