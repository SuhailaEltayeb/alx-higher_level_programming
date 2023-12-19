#!/usr/bin/python3
"""Square class."""


class Square:
    """Square definition."""

    def __init__(my_square, size=0):
        """Constructor.

        Arguements:
            size: side of square ength

        Raises:
            TypeError:If size is not intiger
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        my_square.__size = size
