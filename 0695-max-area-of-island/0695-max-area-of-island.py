class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


       
        max_area=0
        def dfs(r,c,grid):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!=1:
                return 0
            
            
            grid[r][c]=0
            return 1+(
            dfs(r+1,c,grid)+
            dfs(r-1,c,grid)+
            dfs(r,c+1,grid)+
            dfs(r,c-1,grid))




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    max_area=max(max_area,dfs(i,j,grid))
        
        return max_area

        