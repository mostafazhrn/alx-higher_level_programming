#!/usr/bin/python3
"""This module shall produce pascal triangle"""


def pascal_triangle(n):
    """This shall return a list representing trianlge"""

    if n <= 0:
        return []
    else:
        nuevo_lst = []
        for x in range(n):
            nuevo_lst.append([])
            for y in range(x + 1):
                if y == 0 or y == x:
                    nuevo_lst[x].append(1)
                else:
                    nuevo_lst[x].append(nuevo_lst[x - 1][y - 1] +
                                        nuevo_lst[x - 1][y])
        return nuevo_lst
