from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def dfs(startIndex: int, tempSol: list[int], total: int ):

            if startIndex >= len(candidates) or total >  target:
                return
            
            if total == target:
                result.append(tempSol[:])
                return

            for i in range(startIndex, len(candidates)):
                if i> startIndex and candidates[i] == candidates[i-1]:
                    continue

                tempSol.append(candidates[i])
                dfs(i+1, tempSol, candidates[i] + total) # ***
                tempSol.pop()




        dfs(0, [], 0)
        
        return result

'''
Metric	Complexity
Time (worst case)	O(2ⁿ * k)
Space (worst case)	O(R * k + n)
'''







candidates = [10,1,2,7,6,1,5]
target = 8

candidates = [2,5,6,9, 4 ,4] 
target = 9

print(Solution().combinationSum2(candidates, target))
