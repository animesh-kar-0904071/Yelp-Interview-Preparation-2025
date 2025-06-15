class Solution:
    def longestUniqueSubstring(self, givenStr: str) -> str:

        left = 0
        uniqueChars = set()
        maxLength = 0
        longestStr = ''

        for i in range(len(givenStr)):

            while givenStr[i] in uniqueChars:
                uniqueChars.remove(givenStr[left])
                left +=1

            uniqueChars.add(givenStr[i])
            currentLength = i - left + 1
            if currentLength > maxLength:
                maxLength = currentLength
                longestStr = givenStr[left : i + 1]
            #maxLength = max(maxLength, i - left + 1) #2
            
        return longestStr 



sol_instance = Solution()

s = "GEKSFORTGEEKS"
print(sol_instance.longestUniqueSubstring(s))