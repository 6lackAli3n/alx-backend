#!/usr/bin/env python3
"""
0-basic_cache module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that
    inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item in the cache using the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.
        """
        return self.cache_data.get(key, None)
