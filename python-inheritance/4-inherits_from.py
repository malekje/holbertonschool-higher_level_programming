#!/usr/bin/python3
"""True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """True if the object is an instance of a class that inherited"""
    if (type(obj) is not a_class and issubclass(type(obj), a_class)):
        return True
    return False
