# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        cnt=0
        maxVal=float('-inf')
        def cntNodes(node,maxVal):
            nonlocal cnt
            if not node:
                return
            maxVal=max(maxVal,node.val)
            if node.val>=maxVal:
                cnt+=1
            cntNodes(node.left,maxVal)
            cntNodes(node.right,maxVal)
        
        cntNodes(root,maxVal)
        
        return cnt


        