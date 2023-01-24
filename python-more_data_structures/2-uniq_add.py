#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = [my_list[0]]
    for i in range(1, len(my_list)):
        if my_list[i] not in result:
            result.append(my_list[i])
    return sum(result)
