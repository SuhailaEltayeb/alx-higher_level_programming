#!/usr/bin/python3
"""MyList class module."""


class MyList(list):
    """MyList class."""
    def print_sorted(self):
        """print sorted list."""
        print(sorted(self))
