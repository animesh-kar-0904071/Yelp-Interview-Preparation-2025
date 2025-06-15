from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index: int , tempSol: List[int], total: int ): 

            if index >= len(candidates) or total > target:
                return
            
            if total == target:
                res.append(tempSol.copy())
                return
            
            tempSol.append(candidates[index])
            dfs(index, tempSol, total + candidates[index])
            tempSol.pop()
            dfs(index +1, tempSol, total)
            

        dfs(0, [], 0)
        return res
    
    

# T = O(2^n)
# S = (K.T)

candidates = [2,5,6,9] 
target = 9

# candidates = [9,2,2,4,6,1,5]
# target = 8

print(Solution().combinationSum(candidates, target))