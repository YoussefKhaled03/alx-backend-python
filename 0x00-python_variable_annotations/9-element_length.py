#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list l
   of strings as argument and returns a list of integers"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Return a list of tuples, each containing a string and its length"""
    return [(i, len(i)) for i in lst]
