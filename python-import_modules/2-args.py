#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len = len(sys.argv) - 1
    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} argument:".format(len))
    else:
        print("{} arguments:".format(len))
    if len > 0:
        for i in range(1, len + 1):
            print("{0}: {1}".format(i, sys.argv[i]))
