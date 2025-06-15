from collections import deque


class FIFOCache:

    def __init__ (self, capacity):
        self.capacity = capacity
        self.cache = {}
       # self.Q = []
        self.Q = deque()
    

    def get(self, key):
        return self.cache.get(key, -1)
    

    def put(self, key, val):
        if len(self.cache) >= self.capacity:
            #oldest_key  = self.Q.pop(0)
            oldest_key  = self.Q.popleft()
            del self.cache[oldest_key] #***
        
        self.Q.append(key)
        self.cache[key] = val
    


fifo_cache = FIFOCache(3)
fifo_cache.put(1, 'A')
fifo_cache.put(2, 'B')
fifo_cache.put(3, 'C')
print(fifo_cache.get(1))  # Output: 'A'
fifo_cache.put(4, 'D')    # Evicts key 1
print(fifo_cache.get(1))  # Output: -1