#!/usr/bin/env python3
"""This module defines a LRUCache class"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A basic caching system that follows the LRU algorithm"""
    def __init__(self):
        """Initialize the LRUCache class by calling the parent
        class's __init__ method"""
        super().__init__()

    def move_to_end(self, key):
        """Move the specified key to the end of the dictionary"""
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

    def put(self, key, item):
        """
        Assign the item value to the key in the cache data
        dictionary. If the cache is full, discard the least
        recently used item(LRU algorithm)."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.move_to_end(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = list(self.cache_data.keys())[0]
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key in
        the cache data dictionary"""
        if key in self.cache_data and key is not None:
            self.move_to_end(key)
            return self.cache_data[key]
        return None
