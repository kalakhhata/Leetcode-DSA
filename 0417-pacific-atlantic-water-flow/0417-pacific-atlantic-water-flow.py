class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:


        n=len(heights)
        m=len(heights[0])
        pse=set()
        ase=set()
        po=deque()
        ao=deque()

        for i in range(n):
            pse.add((i,0))
            ase.add((i,m-1))
            po.append([i,0])
            ao.append((i,m-1))
        
        for j in range(m):
            pse.add((0,j))
            ase.add((n-1,j))
            po.append([0,j])
            ao.append([n-1,j])

        def dfs(q,seen):
            while q:
                i,j=q.popleft()
                for i_off,j_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r,c=i+i_off,j+j_off
                    if 0<=r<n and 0<=c<m and (r,c) not in seen and heights[r][c]>=heights[i][j]:
                        q.append([r,c])
                        seen.add((r,c))
        
        dfs(po,pse)
        dfs(ao,ase)

        return list(pse.intersection(ase))

        