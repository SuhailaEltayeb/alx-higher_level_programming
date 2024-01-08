#!/usr/bin/python3
"""Rectangle class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle subvlass"""
    def __init__(self, size):
        """Constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square area method"""
        return self.__size ** 2

    def __str__(self):
        """function to return rectangle string representation"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
