#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    keyholder = None
    for key in a_dictionary:
        maxscore = a_dictionary[key]
        break
    for key in a_dictionary:
        if a_dictionary[key] > maxscore:
            maxscore = a_dictionary[key]
            keyholder = key
    return keyholder
