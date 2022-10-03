#!/usr/bin/python3
"""
add arguments to python list
You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
"""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

list = "add_item.json"

try:
    file = load_from_json_file(list)
except:
    file = []

    file.extend(sys.argv[1:])
save_to_json_file(file, list)
