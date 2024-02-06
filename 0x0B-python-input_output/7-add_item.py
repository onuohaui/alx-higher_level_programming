#!/usr/bin/python3
"""
Script: 7-add_item
Adds all arguments to a Python list and saves them to a file
"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    """Main function of the script"""
    filename = "add_item.json"
    items = []

    # Check if the file exists and load its content
    if path.exists(filename):
        items = load_from_json_file(filename)

    # Add arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
