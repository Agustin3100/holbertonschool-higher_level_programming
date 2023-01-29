#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for j in range(x, len):
        try:
            print("{:d}" .format(my_list[j]), end="")
            cnt += 1
        except IndexError:
            return j
    print()
    return cnt
