# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkNode(node1):
            if not node1:
                return False
            
            if isIdentical(node1,subRoot):
                return True
            
            return checkNode(node1.left) or checkNode(node1.right)
        
        def isIdentical(node1,node2):
            if not node1 or not node2:
                return not node1 and not node2
            
            return (node1.val==node2.val and isIdentical(node1.left,node2.left) and isIdentical(node1.right,node2.right))
        
        return checkNode(root)

        