class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        rotton=deque()
        fresh=0
        direction=[(0,1),(0,-1),(-1,0),(1,0)]
        min=0

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    rotton.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        while rotton and fresh>0:
            for _ in range(len(rotton)):
                r,c=rotton.popleft()
                for rd,cd in direction:
                    rr=rd+r
                    cc=cd+c
                    if 0<=rr<row and 0<=cc<col and grid[rr][cc]==1:
                        grid[rr][cc]=2
                        rotton.append((rr,cc))
                        fresh-=1
            min+=1
        return min if fresh<=0 else -1
                        
        


        