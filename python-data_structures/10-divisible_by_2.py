#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = []
    for i in range(len(my_list)):
        if (i % 2 == 0):
            j.insert(my_list[i], True)
        else:
            j.insert(my_list[i], False)
    return j
