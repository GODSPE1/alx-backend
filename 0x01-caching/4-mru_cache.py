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

    def put(self, key, item):
        """
        Assign the item value to the key in the cache data dictionary.
        If the cache is full, discard the most recently used
        item (MRU algorithm).
        """
        if key is None and item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data.popitem()
        self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key in
        the cache data dictionary"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
