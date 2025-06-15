class Solution:

    def isScorePossible(self, points: list[int], target: int) -> bool:
        def dfs(index, total):
            if total == target:
                return True
            if index >= len(points) or total > target:
                return False

            # Choose current point (can reuse, so index stays the same)
            if dfs(index, total + points[index]):
                return True

            # Skip current index
            if dfs(index + 1, total):
                return True

            return False

        return dfs(0, 0)

    #*** like permutation which runs in loop, but the loop starting point is startIndex
    def subsets(self, points: list[int]) -> list[list[int]]: 

        result = []

        def dfs(startIndex: int, tempSol: list[int]):
            # if startIndex >= len(points):
            #     return
            
            result.append(tempSol[:])

            for i in range(startIndex, len(points)): ## diff between permute 

                tempSol.append(points[i])
                dfs(i+1, tempSol)
                tempSol.pop()

        dfs(0, [])

        return result




points = [1,2, 4]
target = 3


print(Solution().isScorePossible(points, target))

print(Solution().subsets(points))
