#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[n]), end='')
            n += 1
        except IndexError:
            break
    print()
    return n
