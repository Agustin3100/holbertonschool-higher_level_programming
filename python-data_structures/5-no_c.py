#!/usr/bin/python3
def no_c(my_string):
    outc = ""
    for i in (my_string):
        if i != 'c' and i != 'C':
            outc += i
    return outc
