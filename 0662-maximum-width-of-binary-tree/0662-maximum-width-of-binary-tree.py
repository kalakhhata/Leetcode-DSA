from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque([(root,0)]) #storing root node and its idx (node,idx)
        max_width=0

        #running while loop till q is not empty
        while q:
            #storing left most node's idx at every level
            left=q[0][1]

            #traversing every node at each level and assigning proper indexes to its child nodes
            for _ in range(len(q)):
                node,idx=q.popleft()
                right=idx
                if node.left:
                    q.append((node.left,2*idx))
                if node.right:
                    q.append((node.right,2*idx+1))
            max_width=max(max_width,right-left+1)
        
        return max_width




        