#!/usr/bin/python3
class LockedClass:
    """
    LockedClass only allows creating the `first_name` attribute dynamically.
    """
    __slots__ = ['first_name']
