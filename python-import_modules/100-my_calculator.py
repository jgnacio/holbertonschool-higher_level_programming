#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    operators = ['+', '-', '*', '/']
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    for op in operators:
        if op == argv[2]:
            if op == '+':
                print("{0} + {1} = {2}".format(a, b, add(a, b)))
            elif op == '-':
                print("{0} - {1} = {2}".format(a, b, sub(a, b)))
            elif op == '*':
                print("{0} * {1} = {2}".format(a, b, mul(a, b)))
            elif op == '/':
                print("{0} / {1} = {2}".format(a, b, div(a, b)))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
