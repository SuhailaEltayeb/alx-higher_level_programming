#!/usr/bin/python3
"""
class Rectangle definition
"""


class Rectangle:
    """class Rectangle representation"""
    def __init__(self, width=0, height=0):
        """rectangle initialization"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """private instance attribute width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance attribute width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance attribute height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
