import math


class Solution:
    def getPrimeFactors(self, num: int) -> list[int]:
        result = []

        # Factor out all 2s
        while num % 2 == 0:
            result.append(2)
            num = num / 2

        # Factor out odd numbers starting from 3   # jump 2
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                result.append(int(i))
                num = num / i

        # If num is a prime number > 2
        if num > 2:
            result.append(int(num))

        return result


        # T = O(logn + √n)
        # S = O(logn + √n)


           




num = 18
num = 48
sol_ins = Solution()
print(sol_ins.getPrimeFactors(num))