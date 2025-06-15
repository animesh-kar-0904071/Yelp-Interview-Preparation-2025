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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None

       
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        

# T = O(logn) --> height of the tree      
        

rootArr = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8

root = listToTree(rootArr)

print(Solution().lowestCommonAncestor(root, TreeNode(p), TreeNode(q)))

