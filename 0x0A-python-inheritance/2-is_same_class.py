#!/usr/bin/python3
"""same object class module."""


def is_same_class(obj, a_class):
    """Detects if object is actually a class instance."""
    return type(obj) == a_class
