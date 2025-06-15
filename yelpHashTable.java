package YELP;

import java.util.LinkedList;



public class yelpHashTable<K,V> {

    private final int SIZE = 10;
    private LinkedList<Entry<K,V>>[] table;
    // c:\Users\User\AppData\Local\Temp\hashtable.webp

    public yelpHashTable() {
        table = new LinkedList[SIZE];
        for (int i = 0; i < SIZE; i ++) {
            table[i] = new LinkedList<>();
        }

    }

    private int hash (K key) {
        return Math.abs(key.hashCode() % SIZE);
    }

    public void put(K key, V value) {

        int index = hash(key);
        LinkedList<Entry<K, V>> bucket = table[index];

        for (Entry<K,V> entry: bucket) {
            if (entry.key.equals(key)){
                entry.val = value;
                return;
            }
        }

        bucket.add(new Entry<K,V>(key, value));
        

    }

    public V get(K key) {

        int index = hash(key);
        LinkedList<Entry<K,V>> bucket  = table[index];

        for ( Entry<K,V> entry: bucket) {

            if (entry.key.equals(key))
                return entry.val;
        }

        return null;
    }

    public void display() {

        for (int i= 0; i < SIZE; i++) {
            System.out.print("Bucket " + i + ": ");
            LinkedList<Entry<K,V>> bucket = table[i];

            for (Entry<K,V> entry : bucket) {
                System.out.println(entry.key + " -->" + entry.val);

            }
            System.out.println();
        }
    }


    
}
