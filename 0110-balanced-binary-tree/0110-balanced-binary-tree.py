# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs(node):
            if not node:
                return 0
            
            lh=dfs(node.left)
            if lh==-1:
                return -1
            
            rh=dfs(node.right)
            if rh==-1:
                return -1
            
            if abs(lh-rh)>1:
                return -1
            
            return max(lh,rh)+1
        
        return dfs(root)!=-1