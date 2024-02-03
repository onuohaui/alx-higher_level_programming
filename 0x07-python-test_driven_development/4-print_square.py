#!/usr/bin/python3
def print_square(size):
    """
    Function that prints a square with the character #.
    Args:
        size: size length of the square (integer)
    Raises:
        TypeError: if size is not an integer or
                   if size is a float and is less than 0.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Print the square or a newline if size is 0
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
        print()

