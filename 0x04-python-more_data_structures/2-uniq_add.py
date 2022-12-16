#!/usr/bin/python3
def uniq_add(my_list=[]):
    from functools import reduce
    if len(my_list) == 0:
        return 0
    return reduce(lambda x, y: x + y, set(my_list))
