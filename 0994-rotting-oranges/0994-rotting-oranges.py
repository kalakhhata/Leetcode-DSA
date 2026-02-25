from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        fresh=0
        rotten=deque()

        #mark the indicies of all rotten oranges with the fresh oranges count
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        minutes=0
        directions=[(0,1),(0,-1),(-1,0),(1,0)]
        #bfs to all rotten oranges and see in how much time 
        #it takes rotten the fresh  4-directionally adjacent oranges
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for dr, dc in directions:
                    rr, cc = i + dr, j + dc
                    if 0 <= rr < row and 0 <= cc < col and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        rotten.append((rr, cc))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh<=0 else -1

        