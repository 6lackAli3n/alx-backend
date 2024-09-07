#!/usr/bin/env python3
""" 4-mru_cache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits
    from BaseCaching and uses MRU caching system """
    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
