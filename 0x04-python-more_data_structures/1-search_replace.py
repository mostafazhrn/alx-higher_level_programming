#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    return ([replace if x == search else x for x in my_list])
