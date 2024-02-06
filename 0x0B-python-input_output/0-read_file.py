#!/usr/bin/python3
"""
Module: 0-read_file
Contains function: read_file
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): Name of the file to be read
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')

if __name__ == "__main__":
    read_file("my_file_0.txt")
