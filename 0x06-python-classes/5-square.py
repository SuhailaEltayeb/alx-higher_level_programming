#!/usr/bin/python3
"""Square class."""


class Square:
    """Square definition."""

    def __init__(self, size=0):
        """Constructor.

        Arguements:
            size: side of square ength
        """
        self.size = size

    @property
    def size(self):
        """square side length property.

        Raises:
            TypeError:If size is not intiger
            ValueError: If size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """square area.

        Returns:
            size by size.
        """
        return self.__size ** 2

    def my_print(self):
        """function to print square."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
