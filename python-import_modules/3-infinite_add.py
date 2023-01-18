#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    list = []
    result = 0
    for num in args:
        num = int(num)
        list.append(num)
    for i in list:
        result += i
    print(result)
