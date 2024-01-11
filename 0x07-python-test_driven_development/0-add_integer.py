#!/usr/bin/python3
"""Addition of 2 intigers module."""


def add_integer(a, b=98):
    """Addition of 2 intigers.

    Args:
        a: 1st integer.
        b: 2nd integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        summation of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
