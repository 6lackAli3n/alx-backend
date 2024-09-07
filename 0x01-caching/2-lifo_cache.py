#!/usr/bin/env python3
"""
2-lifo_cache module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that follows
    the LIFO (Last-In, First-Out) policy.
    When the cache exceeds MAX_ITEMS,
    the most recent added item is discarded.
    """
    def __init__(self):
        """ Initialize the class and call
        the parent constructor """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item in the cache using LIFO strategy.
        """
        if key is not None and item is not None:
            if key not in self.cache_data and len(
                    self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last added item (LIFO)
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            self.cache_data[key] = item
            # Update the last added key
            self.last_key = key

    def get(self, key):
        """
        Get an item from the cache by key.
        """
        return self.cache_data.get(key, None)
