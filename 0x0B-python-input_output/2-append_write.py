#!/usr/bin/python3
"""
Module: 2-append_write
Contains function: append_write
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added
    Args:
        filename (str): Name of the file to append to
        text (str): Text to append to the file
    Returns:
        int: Number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    append_write("file_append.txt", "This School is so cool!\n")
