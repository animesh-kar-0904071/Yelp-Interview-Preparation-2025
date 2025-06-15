from typing import List


class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str)-> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        
        current.endOfWord = True

    def longestPrefix(self) -> str :
        prefix = ""
        node = self.root

        while node and len(node.children) == 1 and not node.endOfWord:
            char = next(iter(node.children)) #**
            prefix += char
            node = node.children[char] 
        
        return prefix


class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:

        if not strs:
            return ""

        trie = Trie()
        for s in strs:
            if s == "":
                return ""
            trie.insert(s)
        
        return trie.longestPrefix()
    
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        longestPrefix = ''
        firstStr = strs[0]

        for i in range(len(firstStr)):
            for s in strs:
                if not s:
                    return ""
                if i == len(s) or s[i] != firstStr[i]:
                    return longestPrefix
                
            
            longestPrefix+= firstStr[i]
        
        return longestPrefix
                                     



strs = ["flower","flow","flight"]

print(Solution().longestCommonPrefix2(strs))


