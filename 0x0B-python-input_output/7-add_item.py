#!/usr/bin/python3
"""Add and saving arguments to a Python list to a file"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        argmts = load_from_json_file("add_item.json")
    except FileNotFoundError:
        argmts = []
    argmts.extend(sys.argv[1:])
    save_to_json_file(argmts, "add_item.json")
