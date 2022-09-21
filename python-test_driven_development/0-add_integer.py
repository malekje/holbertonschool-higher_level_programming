#!/usr/bin/python3
"""
task1

"""
def add_integer(a, b=98):
    """
    return a + b

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
