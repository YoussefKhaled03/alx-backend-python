#!/usr/bin/env python3
"""Type-annotated function type_checking that takes a variable x,
    and returns the type of x"""
from typing import Union, Tuple, List, Any


def type_checking(x: Union[int, float, Tuple[int, int], List[int]]) -> Any:
    """Return the type of x"""
    return (x)
