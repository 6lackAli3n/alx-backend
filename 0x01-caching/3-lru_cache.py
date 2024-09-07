#!/usr/bin/env python3
""" 3-lru_cache module """


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from
    BaseCaching and uses LRU caching system """
    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.usage_order = []  # To track the order of usage

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # If key already exists, we need to update its position
        if key in self.cache_data:
            self.usage_order.remove(key)

            self.cache_data[key] = item
            self.usage_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order since this key was just accessed
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
