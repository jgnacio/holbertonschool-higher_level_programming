#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c_value = ord(str[i])
        if (c_value >= 97 and c_value <= 122):
            c_value -= 32
        print("{}".format(char(c_value)), end='')
    print("")
