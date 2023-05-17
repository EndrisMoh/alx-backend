#!/usr/bin/env python3
""" BasicCache Dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system that doesn't have a limit.

    Attributes:
    cache_data: A dictionary that stores the cached data.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the item value\
                for the key key.

        Args:
          key: The key of the item to be cached.
          item: The value of the item to be cached.

        Raises:
         ValueError: If key or item is None.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key.

        Args:
          key: The key of the item to be retrieved.

        Returns:
          The value of the item in self.cache_data linked to key,\
           or None if key does not exist in self.cache_data.
        """
        if key is None:
            return None
        try:
            self.cache_data[key]
        except KeyError:
            return None
        return self.cache_data[key]
