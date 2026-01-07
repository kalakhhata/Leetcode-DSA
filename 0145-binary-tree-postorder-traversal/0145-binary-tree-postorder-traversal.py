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
        st=[]
        lastVisited=None
        res=[]

        while root or st:
            while root:
                st.append(root)
                root=root.left
            
            node=st[-1]
            if node.right and node.right!=lastVisited:
                root=node.right
            else:
                st.pop()
                res.append(node.val)
                lastVisited=node
        
        return res