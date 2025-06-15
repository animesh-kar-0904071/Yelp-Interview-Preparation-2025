class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        maxSum = nums[0]
        localMaxSum = nums[0]
        for i in range(1, len(nums)):
            localMaxSum = max(nums[i], nums[i] + localMaxSum) # check till now ***
            maxSum = max(maxSum, localMaxSum)

        return maxSum
        






sol_obj = Solution()


nums = [-2,1,-3,4,-1,2,1,-5,4]

nums = [5,4,-1,7,8]

print(sol_obj.maxSubArray(nums))
