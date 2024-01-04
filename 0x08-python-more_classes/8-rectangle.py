#!/usr/bin/python3
"""
class Rectangle definition
"""


class Rectangle:
    """class Rectangle representation"""

    number_of_instances = 0
    """int: number of active instances"""

    print_symbol = '#'
    """type: print symbol, of any type"""

    def __init__(self, width=0, height=0):
        """constructor.


        Args:
            width: Rectangle width
            height: Rectangle height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """returns printable string rectangle reresentation"""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle for new instance"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """print certain message for rectangle deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the giggest rectangle of 2.

        Args:
            rect_1: 1st rectangle
            rect_2: 2nd rectangle
        Raises:
            TypeError: if rect_1 or rect_2 is not instance of rectangle.
        Returns:
            Rectangle with bigger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
