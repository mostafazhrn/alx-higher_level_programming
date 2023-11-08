#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = max(a_dictionary.values())
        for x, y in a_dictionary.items():
            if y == val:
                return (x)
    else:
        return (None)
