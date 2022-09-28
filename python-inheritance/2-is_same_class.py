#!/usr/bin/python3
"""True if the object is exactly an instance of the specified class"""
def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the specified class"""
    if not isinstance(obj, a_class):
        return True
    return False
