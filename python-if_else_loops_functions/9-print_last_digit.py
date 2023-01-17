#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1    # Invert the number to get the last number
    number %= 10        # Get the last digit of the number
    print(number, end='')
    return number
