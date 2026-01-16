# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lv=None
        st=[]
        res=[]
        
        while st or root:
            while root:
                st.append(root)
                root=root.left
            
            node=st[-1]
            if node.right and node.right!=lv:
                root=node.right
            else:
                node=st.pop()
                res.append(node.val)
                lv=node
        return res
        