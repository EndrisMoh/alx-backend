#!/usr/bin/env python3
""" FIFOCache inherits from BasicCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BasicCache
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put adds n item from cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.discard()

        self.cache_data[key] = item

    def get(self, key):
        """get an item from cache"""
        if key is None:
            return None
        try:
            self.cache_data[key]
        except KeyError:
            return None
        return self.cache_data.get(key)

    def discard(self):
        """removes the first item from the cache and prints a message"""
        key = next(iter(self.cache_data.keys()))
        print("DISCARD:", key)
        del self.cache_data[key]
