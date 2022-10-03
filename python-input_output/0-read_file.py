#!/usr/bin/python3
"""Reading file function"""
def read_file(filename=""):
    """Reading file function"""
    with open('UTF8') as filename:
        print(filename.read())

