# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
        p_val=p.val
        q_val=q.val
        curr=root
        while curr:
            parent_val=curr.val
            if p_val<parent_val and parent_val>q_val:
                curr=curr.left
            elif p_val>parent_val and q_val>parent_val:
                curr=curr.right
            else:
                return curr
                



        