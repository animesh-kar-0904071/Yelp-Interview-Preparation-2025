class LIFOCache:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.stack = []


    def get( self, key ):
        # if key not in self.cache.keys():
        #     return -1
        
        return self.cache.get(key, -1) # default reurn -1
    

    def put (self, key, val):
        if len(self.cache) >= self.capacity:
            latest_key = self.stack.pop()
            del self.cache[latest_key]
        
        self.cache[key] = val
        self.stack.append(key)


# Usage
lifo_cache = LIFOCache(3)
lifo_cache.put(1, 'A')
lifo_cache.put(2, 'B')
lifo_cache.put(3, 'C')
print(lifo_cache.get(3))  # Output: 'C'
lifo_cache.put(4, 'D')    # Evicts key 3
print(lifo_cache.get(3))  # Output: -1