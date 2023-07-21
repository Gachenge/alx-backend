#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page
and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index """
    if page < 0 or page_size < 0:
        return None
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
