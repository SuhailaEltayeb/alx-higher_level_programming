#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    check_int = True
    try:
        print("{:d}".format(value))
    except Exception as exp:
        print("Exception:", exp, file=sys.stderr)
        check_int = False
    return check_int
