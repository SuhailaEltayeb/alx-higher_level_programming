#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = 0
    max_key = None
    for x, val in a_dictionary.items():
        if val > max_score:
            max_score = val
            max_key = x
    return max_key
