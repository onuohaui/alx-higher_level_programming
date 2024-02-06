#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Contains function: load_from_json_file
"""

import json

def load_from_json_file(filename):
    """
    Creates an Object from a JSON file
    Args:
        filename (str): Name of the JSON file to load
    Returns:
        obj: Object created from the JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
