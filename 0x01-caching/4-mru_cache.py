#!/usr/bin/env python3
"""This module defines an MRUCache class algorithm implementation"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A basic caching system that follows the Most Recently
    Used (MRU) algorithm"""
    def __init__(self):
        """Initialize the MRUCache class by calling the parent
        class's __init__ method"""
        super().__init__()

    def move_to_end(self, key):
        """Move the specified key to the end of the dictionary"""
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

    def put(self, key, item):
        """
        Assign the item value to the key in the cache data dictionary.
        If the cache is full, discard the most recently used
        item (MRU algorithm).
        """
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard = next(reversed(self.cache_data))
                    del self.cache_data[discard]
                    #removed = self.cache_data.popitem()
                    print("DISCARD:", discard)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key in
        the cache data dictionary"""
        if key is not None and key in self.cache_data:
            self.move_to_end(key)
            return self.cache_data[key]
        return None
