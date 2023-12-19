#!/usr/bin/python3
"""Magic class to print pytcodes."""

import math


class MagicClass:
    """circle class."""

    def __init__(self, radius=0):
        """MagicClass initialization.
        Args:
        radius (float or int): Radius of MagicClas.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculate the area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """calculates the circumference of MagicClass."""
        return (2 * math.pi * self._radius)
