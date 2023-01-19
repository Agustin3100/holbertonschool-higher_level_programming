#!/usr/bin/python3
for i in range(0, 9):
    for k in range(i + 1, 10):
        if(i == 0 and k == 1):
            print("{:d}{:d} ".format(i, k), end='')
        else:
            print(",{:d}{:d} ".format(i, k), end='')
