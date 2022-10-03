#!/usr/bin/python3
"""Reading file function"""
def read_file(filename=""):
    """Reading file function"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
