#!/usr/bin/python3
"""Rectangle class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle subclass"""
    def __init__(self, size):
        """Constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square area function"""
        return self.__size ** 2
