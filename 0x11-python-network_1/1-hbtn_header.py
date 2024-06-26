#!/usr/bin/python3
'''
script to take URL, send request to URL
 display value of the X-Request-Id variable found
in the header of the response.
'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        value = html.get('X-Request-Id')
        print(value)
