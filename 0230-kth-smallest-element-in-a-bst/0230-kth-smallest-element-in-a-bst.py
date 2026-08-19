# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        cnt=0

        curr=root
        st=[]
        prev=None
        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
            
            

            
            curr=st.pop()
            cnt+=1
            if k==cnt:
                return curr.val
            curr=curr.right
        
                
        