#!usr/bin/python3
""" THis script shall find a peak num in lst of unsorted ints"""


def find_peak(arr):
    """This shall find the peak num in lst"""
    big_num = None
    for x in arr:
        if big_num is None or x > big_num:
            big_num = x
    return big_num
