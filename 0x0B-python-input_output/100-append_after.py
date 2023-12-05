#!/usr/bin/python3
"""This module shall insert a line of txt to file"""


def append_after(filename="", search_string="", new_string=""):
    """This Func inserts a line of text after each line with spec str"""
    with open(filename, 'r+', encoding='utf-8') as x:
        nuevo_lst = []
        for ligne in x:
            nuevo_lst.append(ligne)
            if search_string in ligne:
                nuevo_lst.append(new_string)
        x.seek(0)
        x.writelines(nuevo_lst)
