#!/usr/bin/python3
def remove_char_at(str, n):
    cp_str = ''
    for i in range(len(str)):
        if i != n:
            cp_str += str[i]
    return cp_str
