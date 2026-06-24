from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:



        q=deque()
        fresh=0
        time=0

        def check(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!=1:
                return
            q.append([r,c])
            grid[r][c]=2
            fresh-=1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        
        while q and fresh:
            for _ in range(len(q)):
                r,c=q.popleft()

                check(r+1,c)
                check(r-1,c)
                check(r,c+1)
                check(r,c-1)
            
            time+=1
        
        return time if fresh<=0 else -1

        