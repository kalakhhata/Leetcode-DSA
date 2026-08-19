# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        def insert(node):
            if not node:
                return TreeNode(val)
            
            if val<node.val:
                node.left=insert(node.left)
            else:
                node.right=insert(node.right)
            
            return node
        
        return insert(root)
        