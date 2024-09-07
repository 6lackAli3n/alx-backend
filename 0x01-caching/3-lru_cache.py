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
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.popitem(True)
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
