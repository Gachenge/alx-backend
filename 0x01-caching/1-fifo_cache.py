#!/usr/bin/env python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First in first out caching"""
    def __init__(self):
        """initialise the data dictionary"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary the item to the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            items = len(self.cache_data.values())
            if items > BaseCaching.MAX_ITEMS:
                (k := next(iter(self.cache_data)), self.cache_data.pop(k))
                print(f"DISCARD: {k}")

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return(self.cache_data.get(key))
