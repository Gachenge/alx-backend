#!/usr/bin/env python3
"""

class FIFOCache that inherits from BaseCaching and
is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    First in first out caching
    """

    def __init__(self):
        """
        initialise the data dictionary
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary the item to the key
            key -
            item -
        """
        if key is None or item is None:
            pass
        else:
            items = len(self.cache_data)
            if items >= BaseCaching.MAX_ITEMS and\
                    key not in self.cache_data.keys():
                keys = next(iter(self.cache_data.keys()))
                self.cache_data.pop(keys)
                print(f"DISCARD: {keys}")
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
            key -
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data.get(key)
