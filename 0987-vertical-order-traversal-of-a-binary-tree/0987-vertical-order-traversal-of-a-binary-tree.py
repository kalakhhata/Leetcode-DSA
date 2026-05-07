# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        st=[]
        def dfs(row,col,root):
            if not root:
                return
            st.append((col,row,root.val))
            dfs(row+1,col-1,root.left)
            dfs(row+1,col+1,root.right)
        
        dfs(0,0,root)
        st.sort()
        res=[]
        prev_col=None
        for col,row,val in st:
            if prev_col!=col:
                res.append([])
                prev_col=col
            res[-1].append(val)
        
        return res

            

        