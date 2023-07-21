#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page
and page_size
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index """
    if page < 0 or page_size < 0:
        return None
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = self.dataset()
        try:
            first, last = index_range(page, page_size)
            return data[first:last]
        except Exception as e:
            return []
