#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    for k in a_dictionary:
        newdict[k] = a_dictionary[k] * 2
    return newdict
