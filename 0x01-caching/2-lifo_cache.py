#!/usr/bin/env python3
""" LIFOCache inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item to a dictionary
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.discard()

        self.cache_data[key] = item

    def get(self, key):
        """ Return value linked to key
        """
        if key is None:
            return None
        try:
            self.cache_data[key]
        except KeyError:
            return None
        return self.cache_data.get(key)

    def discard(self):
        """removes the last item from the cache and prints a message
        """
        key = next(reversed(self.cache_data.keys()))
        print("DISCARD:", key)
        del self.cache_data[key]
