#!/usr/bin/python3
"""text file insertion function definition."""


def append_after(filename="", search_string="", new_string=""):
    """text insertion after each line containing a given string in a file.

    Args:
        filename (str): file name
        search_string (str): The string to search for.
        new_string (str): The string to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
