#!/usr/bin/python3
def roman_to_int(roman_string):
# create a dictionary with real numbers according to roman ones
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and dict[roman_string[i]] < dict[roman_string[i + 1]]:
            num = num - int(dict[roman_string[i]])
        else:
            num = num + int(dict[roman_string[i]])
    return num
