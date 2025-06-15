from typing import List


class Solution:

    def tripletSum(self, nums: List[int]) -> List[List[int]]:

        resultSet = []
        nums.sort() #*

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            currentVal = nums[i]
            left = i + 1
            right = len(nums) -1

            while (left < right):
            
                sum = currentVal + nums[left] + nums[right]
                if sum == 0:
                    resultSet.append([currentVal, nums[left], nums[right]])
                    left +=1
                    right -=1

                    while left < len(nums) and nums[left] == nums[left -1]:
                        left+=1
                    
                    while right > 0 and nums[right] == nums[right + 1]:
                        right -=1 
                if sum < 0:
                    left+=1
                if sum > 0:
                    right -=1

        return resultSet
      # T = O(N^2) S=O(1)
sol_obj = Solution()

nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [0,0,0]
nums = [-1, -1,0,1,2]

print(sol_obj.tripletSum(nums))