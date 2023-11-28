#!/usr/bin/python3
"""
This is a locked class it shall prevent the user
From creating new instance unless called frstname
"""


class LockedClass:
    """
    This is the locked cls only allow user.
    If lcass named first name
    """
    __slots__ = ["first_name"]
