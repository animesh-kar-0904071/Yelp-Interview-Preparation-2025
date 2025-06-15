class Solution:

    def subtractStrings(self, num1: str, num2: str) -> str:
        
        def isSmaller(a:str, b: str):
            if len(a) != len(b):
                return len(a) < len(b)

            return a < b
        
        negativeCheck = False
        if isSmaller(num1, num2):
            num1, num2 = num2, num1
            negativeCheck = True

        i = len(num1) - 1
        j = len(num2) -1
        borrow = 0
        result = []

        while ( i >= 0):

            digit1 = int(num1[i])
            digit2 = int(num2[j]) if j>=0  else 0

            digit2 += borrow
            if digit1 < digit2:
                digit1 +=10
                borrow = 1
            else:
                borrow = 0

            digit = digit1 - digit2
            result.append(str(digit))
             
            i-=1
            j-=1

        result_str = ''.join(reversed(result)).lstrip('0') #***

        if not result_str:
            return '0'

        return '-' + result_str if negativeCheck else result_str
    


str1 = '123'
str2 = '1123'

print(Solution().subtractStrings(str1, str2))