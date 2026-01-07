# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        self.inOrder(root,res)
        return res

    def inOrder(self,root,res):
        if root:
            self.inOrder(root.left,res)
            res.append(root.val)
            self.inOrder(root.right,res)
        
        