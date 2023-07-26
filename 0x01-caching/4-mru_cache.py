#!/usr/bin/env python3
"""
a class MRUCache that inherits from BaseCaching and is a caching system
"""
from statistics import mode
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """discard most recently used caching"""
    def __init__(self):
        """initialise the class"""
        super().__init__()
        self.lst = []

    def get(self, key):
        """return value in self.cache_data"""
        self.lst.append(key)
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return(self.cache_data.get(key))

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the
        item value for the key key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.lst.append(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                ke = mode(self.lst)
                if ke == 1:
                    ke = self.lst[len(self.lst)]
                self.cache_data.pop(ke)
                print(f"DISCARD: {ke}")
