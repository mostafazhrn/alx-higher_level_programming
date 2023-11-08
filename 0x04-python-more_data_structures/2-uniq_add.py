#!/usr/bin/python3
def uniq_add(my_list=[]):
    for x in my_list:
        if x != 2:
            return (sum(set(my_list)))
