#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j > 96 and j < 123:
            i = chr(j - 32)
        print("{}".format(i), end="")
    print()
