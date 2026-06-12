# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        
        def checkNode(node):
            if not node:
                return False
            
            if isIdentical(node,subRoot):
                return True
            
            return checkNode(node.left) or checkNode(node.right)
        
        def isIdentical(node1,node2):
            if not node1 or not node2:
                return not node1 and not node2
            
            return (node1.val==node2.val and isIdentical(node1.left,node2.left) and isIdentical(node1.right,node2.right))
        
        return checkNode(root)