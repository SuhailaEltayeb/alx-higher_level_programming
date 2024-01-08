#!/usr/bin/python3
"""
MyInt class
"""


class MyInt(int):
    """intiger rebel version"""
    def __new__(cls, *args, **kwargs):
        """New instace creation"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """replacing != with =="""
        return int(self) != other

    def __ne__(self, other):
        """replacing == with !="""
        return int(self) == other

