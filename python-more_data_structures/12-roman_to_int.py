#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != type(""):
        return 0
    roman_string = roman_string.strip()
    roman_string = roman_string.upper()
    roman = {"CM": 900,"CD": 400, "XC": 90, "XL": 40,"IX": 9,"IV": 4,
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_int = 0
    for i in range(0, len(roman_string), 2):
        check = roman_string[i:i + 2]
        if len(check) == 2:
            if check in roman:
                roman_int += roman[check]
            elif roman_string[i] in roman and roman_string[i + 1] in roman:
                roman_int += roman[roman_string[i]] + roman[roman_string[i + 1]]
        else:
            if roman_string[i] in roman:
                roman_int += roman[roman_string[i]]
    return roman_int
