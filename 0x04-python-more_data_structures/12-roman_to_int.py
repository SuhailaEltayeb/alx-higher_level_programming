#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    summation = 0
    n = 0
    Dgts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in reversed(roman_string):
        n = Dgts[x]
        summation += n if summation < n * 5 else -n
    return summation
