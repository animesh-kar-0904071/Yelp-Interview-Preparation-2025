class Solution:

    def dot_product(self, vec1, vec2):
        
        frequency_map_vec1 = {}
        product = 0

        for  vector in vec1:
            frequency_map_vec1[vector[0]] = vector[1]
        
        for vector in vec2:
             if vector[0] in frequency_map_vec1.keys():
                 product += vector[1] * frequency_map_vec1[vector[0]]

                
        return product
    


sol_instance = Solution()
vec1 = [[1, 4], [4,2], [5,3]]
vec2 = [[2, 6], [5,1], [1,7]]

print(sol_instance.dot_product(vec1, vec2))