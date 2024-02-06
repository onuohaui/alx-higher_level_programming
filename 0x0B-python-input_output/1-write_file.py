#!/usr/bin/python3
"""
Module: 1-write_file
Contains function: write_file
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written
    Args:
        filename (str): Name of the file to write to
        text (str): Text to write to the file
    Returns:
        int: Number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    write_file("my_first_file.txt", "This School is so cool!\n")

