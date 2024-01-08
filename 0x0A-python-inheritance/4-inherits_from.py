#!/usr/bin/python3
"""Inherits from method module."""


def inherits_from(obj, a_class):
    """checks if object is a subclass."""
    return isinstance(obj, a_class) and type(obj) != a_class
