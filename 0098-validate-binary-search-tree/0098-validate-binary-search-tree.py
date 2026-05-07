# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        st=[]
        curr=root
        prev=None
        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
            
            curr=st.pop()
            if prev!=None and prev>=curr.val:
                return False
            prev=curr.val
            curr=curr.right
        return True


        