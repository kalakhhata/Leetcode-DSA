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
        

        def dfsBhight(root):
            if not root:
                return 0
            lhight=dfsBhight(root.left)
            if lhight==-1: 
                return -1

            rhight=dfsBhight(root.right)
            if rhight==-1:
                return -1

            if abs(lhight-rhight)>1:
                return -1
            
            return max(lhight,rhight)+1
        
        return dfsBhight(root)!=-1
        