# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm={}
        for i in range(len(inorder)):
            hm[inorder[i]]=i
        q=collections.deque(preorder)
        def build(start,end):
            if start>end:
                return None
            
            val=q.popleft()
            node=TreeNode(val)
            mid=hm[val]
            node.left=build(start,mid-1)
            node.right=build(mid+1,end)
            return node
        
        return build(0,len(inorder)-1)


        