#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len = len(sys.argv)
    print("{} arguments:".format(len - 1))
    if len > 0:
        for i in range(1, len):
            print("{0}: {1}".format(i, sys.argv[i]))
    else:
        print(".")
