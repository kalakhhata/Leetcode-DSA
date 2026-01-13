from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq=deque([root])

        ans=[]
        left_to_right=True
        while dq:
            level=deque()
            for _ in range(len(dq)):
                node=dq.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

           
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ans.append(list(level))
            left_to_right=not left_to_right
        
        return ans

            
            
