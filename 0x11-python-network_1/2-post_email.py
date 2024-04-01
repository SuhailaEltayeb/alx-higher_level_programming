#!/usr/bin/python3
'''
Script to take in a URL and an email, send a POST
request to the passed URL with the email as a parameter
and display the body of  response (decoded in utf-8)
'''
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
