#!/usr/bin/python3
"""This Module is for Add_integar.
For function add_integer
Raises:
It shall raise typeerrors if a b are not int or fl.
"""


def add_integer(a, b=98):
    """
    Return the sum of two integers a & b.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
