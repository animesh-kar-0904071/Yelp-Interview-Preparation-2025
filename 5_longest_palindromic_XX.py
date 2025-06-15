class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxLength = 0
        maxPalindrom = ''

        def coundPalindrom(s:str, left: int, right: int):
            res = {}

            while left >=0 and right < len(s) and s[left] == s[right]:
                # lengthCount += 1
                right += 1 
                left -= 1

            res[s[left +1: right]] = right - left -1

            return res


        # T O(n) (outer loop)×O(n) (each palindrome expansion)=O(n2)
        # S (1)
        for i in range(len(s)):
            # odd palindrom
            resOddLength = coundPalindrom(s, i, i)
            
            for k, v in resOddLength.items():
                if v >= maxLength:
                    maxLength = v
                    maxPalindrom = k

            
            # right palindrom
            resEvenLength = coundPalindrom(s, i, i+1)

            for k, v in resEvenLength.items():
                if v >= maxLength:
                    maxLength = v
                    maxPalindrom = k

            

        return maxPalindrom
            


s = "babad"
s = "cbbd"
s = "abcccdcdd"

print(Solution().longestPalindrome(s))