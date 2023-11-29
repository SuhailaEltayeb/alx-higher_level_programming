#!/usr/bin/python3
def uppercase(str):
    for x in str:
        y = x
        if ord(y) >= 97 and ord(y) <= 122:
            y = chr(ord(x) - 32)
        print("{}".format(y), end='')
    print()
