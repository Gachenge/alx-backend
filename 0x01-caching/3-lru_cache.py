#!/usr/bin/env python3
"""
a class LRUCache that inherits from BaseCaching and
is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """least recently used algorithm"""
    def __init__(self):
        """initialise the class"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionry the item discard items when cache is full"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                (k := next(iter(self.cache_data)), self.cache_data.pop(k))
                print(f"DISCARD: {k}")
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
