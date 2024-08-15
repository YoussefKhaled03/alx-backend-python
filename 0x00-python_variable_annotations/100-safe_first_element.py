#!/usr/bin/env python3
"""Type-annotated function safe_first_element that takes a sequence
  seq of anything and returns its first element."""
from typing import Any, Sequence, Union


def safe_first_element(seq: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the sequence"""
    if seq:
        return seq[0]
    else:
        return None
