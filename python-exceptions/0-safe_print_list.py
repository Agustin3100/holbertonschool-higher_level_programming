#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    for j in range(x):
        try:
            print("{}" .format(my_list[j]), end="")
            cnt += 1
        except IndexError:
            return j
    print()
    return cnt
