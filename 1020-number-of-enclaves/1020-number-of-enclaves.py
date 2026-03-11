class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        cnt=0

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]!=1:
                return
            
            grid[i][j]=-1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(r):
            #left border
            if grid[i][0]==1:
                dfs(i,0)

            #right border
            if grid[i][c-1]==1:
                dfs(i,c-1)
        
        for j in range(c):
            #top border
            if grid[0][j]==1:
                dfs(0,j)
            
            #bottom border
            if grid[r-1][j]==1:
                dfs(r-1,j)

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    cnt+=1
        
        return cnt
