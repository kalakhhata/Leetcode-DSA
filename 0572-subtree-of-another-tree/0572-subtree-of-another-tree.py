# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:






        def checkNode(node):
            if not node:
                return False

            if node.val==subRoot.val and isValid(node,subRoot):
                return True
            
            return checkNode(node.left) or checkNode(node.right)
        
        def isValid(n1,n2):
            if not n1 or not n2:
                return not n1 and not n2
            
            return (n1.val==n2.val and isValid(n1.left,n2.left) and isValid(n1.right,n2.right))
        return checkNode(root)
        