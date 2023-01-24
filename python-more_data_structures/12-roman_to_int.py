#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_string = roman_string.strip()
    roman_string = roman_string.upper()
    roman = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4,
             "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_int = 0
    i = 0
    while i < len(roman_string):
        check = roman_string[i:i + 2]
        if len(check) == 2:
            if check in roman:
                roman_int += roman[check]
                i += 2
            elif roman_string[i] in roman:
                roman_int += roman[roman_string[i]]
                i += 1
        else:
            if roman_string[i] in roman:
                roman_int += roman[roman_string[i]]
                i += 1
    return roman_int
