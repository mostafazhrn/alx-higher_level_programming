#!/usr/bin/python3
"""This module shall print square
Raises:
TypeError: if size is not an integer
ValueError: if size is less than 0
"""


def print_square(size):
    """Print a square
    Args: size (int): length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
