#!/usr/bin/env python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """last in first out caching"""
    def __init__(self):
        """initialise the class"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary the item to the key"""
        if key is not None and item is not None:
            items = len(self.cache_data())
            if items >= BaseCaching.MAX_ITEMS:
                lkey, lvalue = self.cache_data.popitem()
                print(f"DISCARD: {lkey}")
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return(self.cache_data.get(key))
