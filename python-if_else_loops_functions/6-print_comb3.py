#!/usr/bin/python3
for i in range(0, 9):
    for k in range(i + 1, 10):
        if(i == 8 and k == 9):
            break
        print("{:d}{:d}, ".format(i, k), end='')
print("89")
