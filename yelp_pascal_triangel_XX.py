from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []

        for i in range(numRows):

            row = []

            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    last_row = result[-1]
                    row.append( last_row[j-1] + last_row[j] )

            result.append(row)
        
        return result
    


print(Solution().generate(5))