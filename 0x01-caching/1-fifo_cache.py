#!/usr/bin/env python3
"""
create class FIFOCache that inherits from BaseCaching and is a caching system
ou can overload def __init__(self): but don’t forget to call the parent init:
super().__init__()
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First in first out caching
    You must use self.cache_data - dictionary from the parent
    class BaseCaching
    """
    def __init__(self):
        """initialise the data dictionary
        can overload def __init__(self):
        but don’t forget to call the parent init: super().__init__()
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary the item to the key
        If key or item is None, this method should not do anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            items = len(self.cache_data.values())
            if items > BaseCaching.MAX_ITEMS:
                (k := next(iter(self.cache_data)), self.cache_data.pop(k))
                print(f"DISCARD: {k}")

    def get(self, key):
        """return the value in self.cache_data linked to key
        Must return the value in self.cache_data linked to key
        """
        return(self.cache_data.get(key), None)
