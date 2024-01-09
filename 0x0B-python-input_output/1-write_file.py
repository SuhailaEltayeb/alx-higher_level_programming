#!/usr/bin/python3
"""Function to write to a file."""


def write_file(filename="", text=""):
    """Function to write a string to a text file (UTF8).

    Args:
        filename (str): file name to write to.
        text (str): text to be written to file.
    Returns:
        # of chars written to file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
