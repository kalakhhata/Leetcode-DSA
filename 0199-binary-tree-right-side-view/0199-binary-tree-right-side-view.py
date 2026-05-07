from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans=[]
        dq=deque([root])

        while dq:
            ln=len(dq)-1
            for i in range(len(dq)):
                node=dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                if i==ln:
                    ans.append(node.val)
        return ans
                


        