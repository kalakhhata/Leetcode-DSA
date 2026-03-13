class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        fresh=0
        q=deque()
        ans=0
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        while q and fresh>0:

            for _ in range(len(q)):
                rr,cc=q.popleft()
                for rd,cd in dirs:
                    i=rr+rd
                    j=cc+cd
                    if 0<=i<r and 0<=j<c and grid[i][j]==1:
                        grid[i][j]=2
                        q.append((i,j))
                        fresh-=1
            ans+=1
        
        return ans if fresh<=0 else -1




        