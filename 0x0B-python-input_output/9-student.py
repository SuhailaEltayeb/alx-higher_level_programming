#!/usr/bin/python3
"""Student class definition."""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """new Student initialization.

        Args:
            first_name (str): student 1st name.
            last_name (str): student last name.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return student dictionary representation:wq"""
        return self.__dict__
