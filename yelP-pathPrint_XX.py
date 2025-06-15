from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
def listToTree( vals: list[int]) ->  Optional['TreeNode']:

    if not vals or vals[0] is None:
        return None
    
    rootNode = TreeNode(vals[0])

    queue = deque([rootNode])
    i = 1

    while i < len(vals): 
        currentNode = queue.popleft()

        if i < len(vals) and vals[i] is not None:
            leftNode = TreeNode(vals[i])
            currentNode.left = leftNode
            queue.append(leftNode)
        i+=1

        if i < len(vals) and vals[i] is not None:
            rightNode = TreeNode(vals[i])
            currentNode.right = rightNode
            queue.append(rightNode)
        
        i+=1



    return rootNode

class Solution:
    def printPaths(self, root: 'TreeNode') -> list[str]:
        
        if root is None:
            return [""]
        
        result = []
        
        def dfs(node: 'TreeNode', path: str):
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            
            path+= str(node.val)
            
            if node.left:
                dfs(node.left, path + '->')
            if node.right:
                dfs(node.right, path + '->')
            


        
        dfs(root, '')
        return result
    #  T = S = O(n × h)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': # ***

        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        leftNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode = self.lowestCommonAncestor(root.right, p, q)

        if leftNode and rightNode:
            return root
        
        # if not leftNode and not rightNode:
        #     return None
        
        if not leftNode and rightNode:
            return rightNode
        
        if leftNode and not rightNode:
            return leftNode
        
        #return  leftNode != None  ? leftNode : rightNode 
        return leftNode if leftNode else rightNode
        

        '''
        ✅ Time Complexity

            You visit each node once in the worst case.

            So, the time complexity is:

            O(N)

        Where:

            N is the number of nodes in the binary tree.

        Even if p and q are found early, the worst-case scenario is still traversing the entire tree (e.g., p and q are leaves on opposite ends).
        ✅ Space Complexity

            The recursive call stack is proportional to the height of the tree.

        Worst-case height:

            Balanced tree → height = O(log N)

            Unbalanced tree → height = O(N)
        
        '''
        
        

        

        

# T = O(logn) --> height of the tree      
        

rootArr = [3,5,1,6,2,0,8,None,None,7,4]



rootArr = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1

root = listToTree(rootArr)

print(Solution().lowestCommonAncestor(root, TreeNode(p), TreeNode(q)))

#print(Solution().printPaths(root))

###print(Solution().lowestCommonAncestor(root, TreeNode(p), TreeNode(q)))

