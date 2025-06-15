package YELP;

import java.util.Deque;
import java.util.LinkedList;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.locks.ReentrantLock;

class LRUCache<K,V> {

    private final int capacity;
    private final ConcurrentHashMap<K, V> map;
    private final Deque<K> deque;
    private final ReentrantLock lock = new ReentrantLock();


    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new ConcurrentHashMap<>(capacity);
        this.deque = new LinkedList<>();
    }

    public V get(K k) {
        V val = map.get(k);
        
        if (val != null) {
            lock.lock();
            try {
                deque.remove(k);                
                deque.addFirst(k);
            } finally {
                lock.unlock();
            }
            
        }

        return val;
    }

    public void put(K k, V v) {
        lock.lock();

        try {
            // already there, re-setting the value
            if (map.contains(k)) {
                deque.remove(k);
                //deque.addFirst(k);
              // a new key comes 
            } else if (map.size() >= this.capacity) {
                K last_key = deque.removeLast();
                map.remove(last_key);
            }
            map.put(k, v);
            deque.addFirst(k);
        } catch (Exception e ) {
            // log or throw something based on subclass exception
        } finally {
            lock.unlock();
        }
    }

    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        LRUCache lru = new LRUCache(3);

        lru.put(1, 'A');
        lru.put(2, 'B');
        lru.put(3, 'C');

        lru.get(2);
        lru.put(1, 4);
        
    }


}
