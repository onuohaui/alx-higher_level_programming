#!/usr/bin/python3
"""
Module for appending text after specific lines in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file to append to.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing the search string.

    Returns:
        None
    """
    buffer = []
    with open(filename, 'r') as f:
        for line in f:
            buffer.append(line)
            if search_string in line:
                buffer.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(buffer)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
