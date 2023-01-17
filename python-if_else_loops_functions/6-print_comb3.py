#!/usr/bin/python3
for left in range(10):
    for right in range(1,10):
        if (left < right):
            print("{}{}".format(left, right), end=", ")
