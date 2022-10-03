#!/usr/bin/python3
"""writing file function"""


def write_file(filename="", text=""):
    """writing file function"""
    with open(filename, "w",encoding="utf-8") as file:
        return(file.write(text))
