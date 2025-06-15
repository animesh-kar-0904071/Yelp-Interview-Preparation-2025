class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    
    def get(self, key):

        if key not in self.cache.keys():
            return -1
        
        self.stack.remove(key) # remove by value **
        self.stack.append(key)
        return self.cache[key]


    def put(self, key, val):

        if key in self.cache:
            self.stack.remove(key) # value [1, 2, 3, 2]
        elif len(self.cache) >= self.capacity:
            last_used_key = self.stack.pop()
            del self.cache[last_used_key]


        self.cache[key] = val
        self.stack.append(key)


mru_cache = MRUCache(3)
mru_cache.put(1, 'A')
mru_cache.put(2, 'B')
mru_cache.put(3, 'C')
print(mru_cache.get(2))  # Output: 'B'
mru_cache.put(4, 'D')    # Evicts key 2
print(mru_cache.get(2))  # Output: -1