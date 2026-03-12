class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+=1
                    self.dfs(i,j,grid)
        
        return ans

    def dfs(self,r,c,grid):
        if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!='1'):
            return
        grid[r][c]='-1'
        self.dfs(r+1,c,grid)
        self.dfs(r-1,c,grid)
        self.dfs(r,c+1,grid)
        self.dfs(r,c-1,grid)
        


        
        