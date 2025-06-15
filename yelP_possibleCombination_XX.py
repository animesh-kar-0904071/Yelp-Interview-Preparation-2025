class Solution:
    def generate_permutations(self, s: str) -> list[str]:

        result = []
        
        def backTrack(tempSol: list, used: set):

            if len(s) == len(tempSol):
                result.append(tempSol[:])
                return
            
            for i in range(len(s)):

                # if s[i] in tempSol:
                #     continue

                if s[i] in used:
                    continue

                tempSol.append(s[i])
                used.add(s[i])
                backTrack(tempSol, used)
                tempSol.pop()
                used.remove(s[i])

        backTrack([], set())
        return result
    
    # T = S = O(n * N!)
    
    
    def generate_combinations(self, s: str) -> list[str]:
        result = []

        def backtrack(index: int, path: list[str]):
            if index == len(s):
                result.append(''.join(path))
                #result.append(path[:])
                return

            char = s[index]
            if char.isalpha():
                # Lowercase branch
                path.append(char.lower())
                backtrack(index + 1, path)
                path.pop()
                
                path.append(char.upper())
                backtrack(index + 1, path)
                path.pop()
            else:
                # Non-letter characters are added directly
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result



s= "0ab" 
#print(Solution().generate_permutations(s))
print(Solution().generate_combinations(s))