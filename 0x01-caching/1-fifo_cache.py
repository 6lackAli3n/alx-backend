#!/usr/bin/env python3
"""
1-fifo_cache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that follows
    the FIFO (First-In, First-Out) policy.
    When the cache exceeds MAX_ITEMS,
    the oldest added item is discarded.
    """
    def __init__(self):
        """ Initialize the class and
        call the parent constructor """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache using FIFO strategy.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
    """Retrieves an item by key.
    """
    return self.cache_data.get(key, None)
