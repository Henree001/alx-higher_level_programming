#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            newstring += i
    return newstring
