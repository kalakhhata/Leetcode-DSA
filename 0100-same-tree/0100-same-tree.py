# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs(n1,n2):
            if (not n1 and not n2):
                return True
            elif (not n2 or not n1):
                return False
            elif n1.val!=n2.val:
                return False
            
            lh=dfs(n1.left,n2.left)
            rh=dfs(n1.right,n2.right)

            return lh and rh
        
        return dfs(p,q)
            