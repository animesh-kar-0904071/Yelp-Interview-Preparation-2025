package YELP;

import java.util.PriorityQueue;

public class kthLargest {

    // Function to find the K'th largest element
    public static int kthLargestE(int[] arr, int K) {
      
        PriorityQueue<Integer> pq  = new PriorityQueue<>(); // Collections.reverseOrder()

        for (int num : arr ) {
            pq.add(num);
            if (pq.size() > K) {
                pq.poll();
            }
        }

        return pq.poll();

        // n log K

    }

    public static void main(String[] args) {
        int[] arr = {12, 3, 5, 7, 19};
        int K = 2;
        System.out.println(kthLargestE(arr, K));
    }
    
}
