#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that adds 2 integers.
    Args:
        a (int or float): The first parameter.
        b (int or float): The second parameter (default 98).
    Returns:
        int: The addition of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
