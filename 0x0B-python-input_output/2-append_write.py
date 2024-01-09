#!/usr/bin/python3
"""Function to append text to the end of file"""


def append_write(filename="", text=""):
    """Appending string to the end of file.

    Args:
        filename (str): file name to append text to.
        text (str): text string to be appended to file
    Returns:
        # of chars appended to file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
