class Solution:

    left_parentheses = '('
    right_parentheses = ')'
    left_braces = '{'
    right_braces = '}'
    left_brackets = '['
    right_brackets = ']'

    def isMatchingPair(self, c1, c2) -> bool:

        if c1 == self.left_parentheses and c2 == self.right_parentheses:
            return True
        elif c1 == self.left_braces and c2 == self.right_braces:
            return True
        elif c1 == self.left_brackets and c2 == self.right_brackets:
            return True
        else:
            return False


    def isBalanced(self, s: str )-> bool:
        
        stack = []

        for i in range(len(s)):
            if s[i] == self.left_parentheses or s[i] == self.left_braces or s[i] == self.left_brackets:
                stack.append(s[i])
            elif s[i] == self.right_parentheses or s[i] == self.right_braces or s[i] == self.right_brackets:
                if len(stack) == 0:
                    return False
                elif not self.isMatchingPair(stack.pop() , s[i]):
                    return False



        return len(stack) == 0 




s = "{}[()]{(())}}"

sol_instance = Solution()

print(sol_instance.isBalanced(s))