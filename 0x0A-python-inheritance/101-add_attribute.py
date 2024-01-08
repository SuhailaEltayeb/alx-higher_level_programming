#!/usr/bin/python3
"""Function to add  attributes to objects."""


def add_attribute(obj, att, value):
    """Adding attribute to object if possible.
    Args:
        obj (any): object to add  attribute to.
        att (str): attribute name.
        value (any): attribute value.
    Raises:
        TypeError: If not possible to add attribute to object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

