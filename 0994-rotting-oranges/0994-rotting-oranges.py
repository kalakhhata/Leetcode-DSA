class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


       
        
        q=deque()
        fresh=0
        n=len(grid)
        m=len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        def addOranges(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>=n or c>=m or grid[r][c]!=1:
                return
            grid[r][c]=2
            q.append((r,c))
            fresh-=1

        time=0
        while q and fresh:

            for i in range(len(q)):
                r,c=q.popleft()
                addOranges(r+1,c)
                addOranges(r-1,c)
                addOranges(r,c+1)
                addOranges(r,c-1)
            time+=1
        
        return -1 if fresh!=0 else time

        