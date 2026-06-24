class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row=len(heights)
        col=len(heights[0])

        pq=deque()
        pse=set()

        aq=deque()
        ase=set()

        for i in range(row):
            pq.append([i,0])
            aq.append([i,col-1])
            pse.add((i,0))
            ase.add((i,col-1))
        
        for j in range(col):
            pq.append([0,j])
            aq.append([row-1,j])
            pse.add((0,j))
            ase.add((row-1,j))

        
        
        def bfs(que,seen):
            while que:
                i,j=que.popleft()
                for ioff,joff in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r=i+ioff
                    c=j+joff
                    if 0<=r<row and 0<=c<col and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append([r,c])
        
        bfs(pq,pse)
        bfs(aq,ase)

        return list(pse.intersection(ase))

                    

        
        
        