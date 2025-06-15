class Solution:
    def isSubSequence(self, word: str, s1:str)-> bool:

        i = 0

        for ch in s1:
            if i < len(word) and ch == word[i]:
                i+=1

        return i == len(word)
    
    
    def numMatchingSubseq(self, s1: str, words: list[str])-> int:

        count = 0

        for word in words:
            if self.isSubSequence(word, s1):
                count +=1

        return count
    
  # T = O(n * m)


# Example 1
s1 = "abcde"
words1 = ["a", "bb", "acd", "ace"]
print(Solution().numMatchingSubseq(s1, words1))  # Output: 3


# Example 2
s2 = "dsahjpjauf"
words2 = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
print(Solution().numMatchingSubseq(s2, words2))  # Output: 2