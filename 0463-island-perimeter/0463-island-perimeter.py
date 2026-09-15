class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt=0
        def dfs(r,c,grid):
            nonlocal cnt
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0:
                cnt+=1
                return
            if grid[r][c]==-1:
                return
            
            grid[r][c]=-1
            dfs(r+1,c,grid)
            dfs(r-1,c,grid)
            dfs(r,c+1,grid)
            dfs(r,c-1,grid)

            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dfs(i,j,grid)
        return cnt