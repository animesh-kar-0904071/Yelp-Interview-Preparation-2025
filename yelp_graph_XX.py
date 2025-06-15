from collections import defaultdict
import random
from typing import Optional


class Solution:

    '''
    📊 Complexity

    Time Complexity:

        Best case (no edge rejections): O(e)

        Worst case (many rejections near limit): O(e × n²)

    Space Complexity:

        graph: O(n + e)

        edges: O(e)
    '''
    def buildUndirectedGraph(self, n: int, e: int):
        if e > n * (n - 1) // 2:
            raise ValueError('too many edges')
        # if e == n:
        #     raise ValueError('')
        
        graph = defaultdict(list)
        edges = set()

        while len(edges) < e:
            u = random.randint(0, n -1)
            v = random.randint(0, n -1)

            if u!=v and (u,v) not in edges and (v,u) not in edges:
                graph[u].append(v)
                graph[v].append(u)
                edges.add((u,v))
        

        return graph
    

    '''
    📊 Complexity

    Time Complexity:

        Best case (no edge rejections): O(e)

        Worst case (many rejections near limit): O(e × n²)

    Space Complexity:

        graph: O(n + e)

        edges: O(e)
    '''
    def buildDirectedGraph(self, n: int, e: int):
        if e > n * (n - 1):
            raise ValueError('too many edges')
        
        graph = defaultdict(list)
        edges = set()

        while len(edges) < e:
            u = random.randint(0, n - 1)
            v = random.randint(0, n -1)

            if u != v and (u,v) not in edges:
                graph[u].append(v)
                edges.add((u,v))

        
        return graph
        

    



print(Solution().buildUndirectedGraph(3, 3))

print(Solution().buildDirectedGraph(3, 3))
            
        