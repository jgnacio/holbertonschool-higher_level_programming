#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a == 0 and len_b > 0:
        return tuple_b
    if len_b == 0 and len_a > 0:
        return tuple_a
    if len_a < 2:
        snumber_a = 0
    else:
        snumber_a = tuple_a[1]
    if len_b < 2:
        snumber_b = 0
    else:
        snumber_b = tuple_b[1]
    new_tuple = (tuple_a[0] + tuple_b[0], snumber_a + snumber_b)
    return new_tuple
