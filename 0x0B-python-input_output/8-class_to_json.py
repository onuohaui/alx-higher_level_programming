#!/usr/bin/python3
"""
Module: 8-class_to_json
Contains function: class_to_json
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representing the attributes of the object.
    """
    return obj.__dict__
