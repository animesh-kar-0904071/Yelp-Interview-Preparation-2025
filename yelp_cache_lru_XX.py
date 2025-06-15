'''
What LRU Means

LRU stands for “Least Recently Used.” In an LRU caching system, the least recently accessed data is removed first when the cache reaches its limit. This approach is based on the principle that data accessed least recently is less likely to be needed in the future.
LRU (Least Recently Used) Cache Example

An LRU cache evicts the least recently accessed entries first.
'''

from typing import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    '''
    @param key 
    returns value if found else -1
    '''
    def get(self, key):

        if key not in self.cache.keys():
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
    
    '''
    @param key 
    returns value if found else -1
    '''
    def put(self, key, val):
        if key in self.cache.keys():
            self.cache.move_to_end(key)

        self.cache[key] = val
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) #****                             


        


# Usage
lru_cache = LRUCache(3)
lru_cache.put(1, 'A')
lru_cache.put(2, 'B')
lru_cache.put(3, 'C')
print(lru_cache.get(1))  # Output: 'A'
lru_cache.put(4, 'D')    # Evicts key 2
print(lru_cache.get(2))  # Output: -1
        