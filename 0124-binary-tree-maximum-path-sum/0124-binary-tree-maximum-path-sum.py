# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float('-inf')
        def maxPathSum(node):
            nonlocal maxi
            if not node:
                return 0
            
            lsum=max(0,maxPathSum(node.left))
            rsum=max(0,maxPathSum(node.right))
            maxi=max(maxi,lsum+rsum+node.val)

            return node.val+max(lsum,rsum)
        
        maxPathSum(root)
        return maxi

        
        