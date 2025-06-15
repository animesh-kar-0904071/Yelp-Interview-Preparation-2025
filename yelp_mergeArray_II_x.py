from typing import List


class Solution:
    def move_to_end(self, a: List[int]):
        size = len(a)
        j = size - 1
        for i in range(size - 1, -1, -1):
            if a[i] is not None:
                a[j] = a[i]
                if i != j:
                    a[i] = None
                j-=1

        return j+1

        

    def merge(self, a: List[int], b: List[int]):
        
        
        n = len(b)
        i = self.move_to_end(a)
        k = 0
        j = 0
        total = len(a)
        # a = [N, N, N, N, 2, 8, 13, 15, 20]

        while k < total:

            if i < total and (j == n or a[i] <= b[j]):
                a[k] = a[i]
                i+=1
            else:
                a[k] = b[j]
                j+=1
            
            k+=1


# Test the code
a = [2, 8, None, None, None, None, 13, None, 15, 20]
b = [3, 5, 7, 9, 25]

Solution().merge(a, b)
print(a)