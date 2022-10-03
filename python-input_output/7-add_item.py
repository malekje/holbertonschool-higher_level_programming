#!/usr/bin/python3
"""adds all arguments to a Python list"""
import sys


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

list = "add_item.json"

try:
    file = load_from_json_file(list)
except FileNotFoundError:
    file = []
save_to_json_file(list, "add_item.json")