#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = None
    name = None
    for key in a_dictionary:
        if score is None:
            score = a_dictionary[key]
            name = key
        elif a_dictionary[key] > score:
            score = a_dictionary[key]
            name = key
    return name
