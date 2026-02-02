# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self,root,reverse=False):
        self.stack=[]
        self.reverse=reverse
        self._pushAll(root) 
        #_ (underscore) doesnt stop this function to run from outside but it just instruct devloper that it is for inside use only
    
    def _pushAll(self,node):
        while node:
            self.stack.append(node)
            node=node.right if self.reverse else node.left
    
    def next(self):
        temp=self.stack.pop()
        self._pushAll(temp.left if self.reverse else temp.right)
        return temp.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l=BSTIterator(root)
        r=BSTIterator(root,True)

        i=l.next()
        j=r.next()

        while i<j:
            if i+j==k:
                return True
            elif i+j>k:
                j=r.next()
            else:
                i=l.next()
        
        return False
        