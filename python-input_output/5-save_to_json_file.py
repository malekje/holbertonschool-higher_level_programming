#!/usr/bin/python3
"""writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, "w") as file:
        return(file.write(my_obj))
