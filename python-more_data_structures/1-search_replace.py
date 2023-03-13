#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in new_list:
        if (search in new_list == True) or i == search:
            new_list.insert(i, replace)
            new_list.pop(i - 1)
    return new_list
