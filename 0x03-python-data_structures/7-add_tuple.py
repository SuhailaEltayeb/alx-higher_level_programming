#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num_a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    num_a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    num_b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    num_b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (num_a1 + num_b1, num_a2 + num_b2)
