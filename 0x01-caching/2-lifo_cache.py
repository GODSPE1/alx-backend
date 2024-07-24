#!/usr/bin/env python3
"""This module defines a LIFOCache class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A basic caching system that follows the LIFO algorithm"""
    def __init__(self):
        """Initialize the FIFOCache class by calling
        the parent class's __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign the item value to the key in the cache data dictionary.
        If the cache is full, discard the recently added item (LIFO algorithm).
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = list(self.cache_data)
                self.cache_data.pop(discard[-1])
                print("DISCARD:", discard)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the
        given key in the cache data dictionary
        """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
