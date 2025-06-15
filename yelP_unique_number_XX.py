class Solution:

    def find_difference(self, arr1: list[int], arr2:list[int]) -> int: #***

        result = 0

        for num in arr1 + arr2: #*
            result ^= num

        return result
    

    def find_difference2(self, arr1: list[int], arr2:list[int]) -> int: # only for positive, we can also use hashset

        arr1Sum = sum(arr1)
        arr2sum = sum(arr2)

        return abs(arr1Sum - arr2sum)


arr1 = [1, 2, 3]
arr2 = [1, 2, 3, -5]


print(Solution().find_difference(arr1, arr2))