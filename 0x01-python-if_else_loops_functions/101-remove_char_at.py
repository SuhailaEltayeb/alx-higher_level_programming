#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    i = 0
    for char in str:
        if i != n:
            copy += str[i]
        i += 1
    return (copy)
