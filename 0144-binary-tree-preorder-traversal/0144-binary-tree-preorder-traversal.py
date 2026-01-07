# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #here to find the preorder traversal we gonna use stack(LIFO) 
        #so It goes like root-left-right
        #we add the root level and check if there is any right/left nodes there if there are we add right and left in order
        #since its LIFO it will always give us left node to explore 

        if not root:
            return []

        st=[]
        res=[]
        st.append(root)

        while st:
            r=st.pop() #It will give us last node to explore
            res.append(r.val)
            if r.right:
                st.append(r.right)
            if r.left:
                st.append(r.left)
        return res


        