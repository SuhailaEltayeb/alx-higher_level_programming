#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    replaced_list = my_list.copy()
    replaced_list[idx] = element
    return replaced_list
