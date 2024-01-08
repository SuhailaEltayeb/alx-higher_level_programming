#!/usr/bin/python3
"""Lookup function module."""


def lookup(obj):
    """finds object methods and attributes .
    Args:
        obj (object): object.

    Returns:
        list: Attributes list.
    """
    return dir(obj)
