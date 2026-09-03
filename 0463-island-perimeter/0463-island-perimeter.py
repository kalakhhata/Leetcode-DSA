class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        perimeter=0
        n=len(grid)
        m=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if i>0 and grid[i-1][j]==0 or i==0:
                        perimeter+=1
                    if j>0 and grid[i][j-1]==0 or j==0:
                        perimeter+=1
                    if i<n-1 and grid[i+1][j]==0 or i==n-1:
                        perimeter+=1
                    if j<m-1 and grid[i][j+1]==0 or j==m-1:
                        perimeter+=1
        return perimeter

                    
        
