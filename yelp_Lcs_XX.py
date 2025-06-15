class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1

        #dp = [0] * rows 
        dp = [ [0] * cols for _ in range(rows)]

        for i in range(1, rows):
            for j in range(1, cols):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1] # 1 + left[immediate_corner]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        

        lcs = []

        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                lcs.append(text1[i-1]) 
                i-=1
                j-=1
            if dp[i-1][j] > dp [i][j-1]:
                i-=1
            else:
                j-=1

        lcs.reverse()

        print(''.join(lcs))



        return dp[-1][-1]
    




s1 = 'abcdebdk'
s2 = 'acek'

print(Solution().longestCommonSubsequence(s1,s2))