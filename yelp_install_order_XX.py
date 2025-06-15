from collections import defaultdict

class Solution:
    '''
        🔁 What the Code Does

        It builds a graph from the list of dependencies, then performs a DFS-based topological sort to find a valid installation order of the packages, while detecting cycles (like in a directed acyclic graph, DAG).
        ✅ Assumptions

        Let:

            n = number of packages

            e = number of dependencies

            Let packages be the list of all nodes you want an install order for.

            Dependencies are pairs like [a, b] meaning a depends on b, so b must be installed before a.

        🧠 Time Complexity

            Building the graph:

                for a, b in dependencies: O(e)

            DFS traversal:

                In worst case, every node is visited once → O(n)

                For each node, we visit all its neighbors → O(e)

            ✅ So, total DFS cost: O(n + e)

        🧠 Space Complexity

            Graph (adjacency list): O(n + e)

            Visited/Visiting sets: O(n)

            Call stack for DFS (recursion): O(n) in the worst case

            Install order list: O(n)

        ✅ Total space: O(n + e)
        ✅ Final Answer

            Time Complexity: O(n + e)

            Space Complexity: O(n + e)
    '''
    def findInstallOrder(self, dependencies: list[list[str]], packages: list[str]) -> list[str]:
        

        #Step 1: Build adjacency list
        graph = defaultdict(list)
        for a, b in dependencies:
            graph[a].append(b)

        visiting = set()
        visited = set()
        install_order = []
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        def dfs(node: str) -> bool:
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
                
            visiting.remove(node)
            visited.add(node)
            install_order.append(node)
            return True

        # Step 1: DFS on each node
        for package in packages:
                if not dfs(package):
                    return []  # cycle detected

        # Step 4: Convert back to names and reverse
        return install_order


sol_obj = Solution()
packages = ["a", "b", "c", "d", "e"]
dependencies = [["a", "b"], ["b", "c"], ["b", "d"], ["c", "e"],  ["d", "e"]]
print(sol_obj.findInstallOrder(dependencies, packages))  # Expected: ['e', 'c', 'd', 'b', 'a']