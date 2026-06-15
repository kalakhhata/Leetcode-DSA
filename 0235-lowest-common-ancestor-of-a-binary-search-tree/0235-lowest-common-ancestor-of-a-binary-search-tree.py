# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval=p.val
        qval=q.val

        curr=root
        while curr:
            lca=curr.val

            if pval<lca and lca>qval:
                curr=curr.left
            elif pval>lca and qval>lca:
                curr=curr.right
            else:
                return curr
        
        return None
        