#!/usr/bin/python3
"""Base class module"""
from json import dumps, loads


class Base:
    """Base class representation."""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
