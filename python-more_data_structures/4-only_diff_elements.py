#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_2 - set_1 | set_1 - set_2
    return new_set
