#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    ldigit = number % 10
    print("{}".format(ldigit), end='')
    return (ldigit)
