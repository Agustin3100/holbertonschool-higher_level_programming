def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            cnt += 1
        except ValueError:
            cnt += 0
        except TypeError:
            cnt += 0
    print("")
    return (cnt)
