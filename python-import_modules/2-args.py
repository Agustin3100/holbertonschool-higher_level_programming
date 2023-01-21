#!/usr/bin/python3
import sys
if (len(sys.argv) == 1):
    print("0 arguments.")
elif (len(sys.argv) == 2):
    print("1 argument:")
    for i in range(len(sys.argv)-1):
        print("{}: {}".format(len(sys.argv)-1, sys.argv[i + 1]))
elif (len(sys.argv) >= 2):
    print("{} arguments:".format(len(sys.argv)-1))
    for i in range(1, len(sys.argv)-1):
        print("{}: {}".format((i), sys.argv[i]))
