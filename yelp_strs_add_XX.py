class Solution:
    def add(self, num1:str, num2:str) -> str:
        result = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0

        while(i >= 0 or j>= 0 or carry): #*** 999 + 100

            digit1 = int(num1[i]) if i>=0 else 0
            digit2 = int(num2[j]) if j>=0 else 0

            total = carry + digit1 + digit2
            carry = int (total / 10)
            digit = total % 10
            result.append(str(digit))

            i-=1
            j-=1


        return ''.join(reversed(result))
    



sol_ins = Solution()
str1 = '123'
str2 = '4577'

print(sol_ins.add(str1, str2))

