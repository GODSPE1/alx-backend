#!/usr/bin/env python3
"""This module defines an MRUCache class algorithm implementation"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A basic caching system that follows the MRU algorithm"""
    def __init__(self):
        """Initialize the MRUCache class by calling the parent
        class's __init__ method"""
        super().__init__()

    def put(self, key, item):
        """discard the most recently used item (MRU algorithm)."""
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard = next(reversed(self.cache_data))
                    del self.cache_data[discard]
                    # removed = self.cache_data.popitem()
                    print("DISCARD:", discard)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key data dictionary"""
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
