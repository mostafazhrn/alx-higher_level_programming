#!/usr/bin/python3
"""This module prints a text with 2 new.
Ln after each character as follows: ., ? and :
Raises:
TypeError: if text is not a string
"""


def text_indentation(text):
    """Print txt with 2 new lines chars.
    Args are text (str) which is text to print
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    for x in range(x, len(text)):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == '':
                x += 1
