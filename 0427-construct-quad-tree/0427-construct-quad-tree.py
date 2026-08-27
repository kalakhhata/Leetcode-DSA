"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def allSame(grid,x,y,n):
            val=grid[x][y]
            for i in range(x,x+n):
                for j in range(y,y+n):
                    if grid[i][j]!=val:
                        return False
            return True
        def solve(grid,x,y,n):
            if allSame(grid,x,y,n):
                return Node(grid[x][y],True)
            else:
                node=Node(True,False)
                node.topLeft=solve(grid,x,y,n/2)
                node.topRight=solve(grid,x,y+n/2,n/2)
                node.bottomLeft=solve(grid,x+n/2,y,n/2)
                node.bottomRight=solve(grid,x+n/2,y+n/2,n/2)
            return node
        
        return solve(grid,0,0,len(grid))
        
        