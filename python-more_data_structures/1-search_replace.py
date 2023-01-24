#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, element in enumerate(new_list):
        if element == search:
            new_list[i] = replace
    return new_list
