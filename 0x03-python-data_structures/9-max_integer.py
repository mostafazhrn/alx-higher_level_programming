#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = my_list[0]
    for x in my_list:
        if x > max_num:
            max_num = x
    return (max_num)
