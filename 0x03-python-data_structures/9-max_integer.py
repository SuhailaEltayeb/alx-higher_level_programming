#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list)) < 1:
            return None
    replica = my_list.copy()
    replica.sort()
    return replica[-1]
