# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        self.postOrder(root,res)
        return res
    
    def postOrder(self,root,res):
        if root:
            self.postOrder(root.left,res)
            self.postOrder(root.right,res)
            res.append(root.val)
    
    