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
            pse.add((i,0))
            aq.append([i,col-1])
            ase.add((i,col-1))
        
        for j in range(col):
            pq.append([0,j])
            pse.add((0,j))
            aq.append([row-1,j])
            ase.add((row-1,j))
        
        def bfs(q,seen):
            while q:
                i,j=q.popleft()
                for ioff,joff in [(1,0),(-1,0),(0,1),(0,-1)]:
                    r,c=i+ioff,j+joff
                    if 0<=r<row and 0<=c<col and (r,c) not in seen and heights[r][c]>=heights[i][j]:
                        q.append([r,c])
                        seen.add((r,c))
        
        bfs(pq,pse)
        bfs(aq,ase)

        return list(pse.intersection(ase))



        