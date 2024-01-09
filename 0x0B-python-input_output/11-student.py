#!/usr/bin/python3
"""Student class definition."""


class Student:
    """student representation."""

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

    def to_json(self, attrs=None):
        """return student dictionary representation.

        If attrs is string list, only represents attributes
        included in list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all student attributes.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
