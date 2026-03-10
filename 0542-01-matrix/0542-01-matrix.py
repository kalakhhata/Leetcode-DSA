class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r=len(mat)
        c=len(mat[0])
        q=deque()
        dir=[(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=float('inf')
        
        while q:
            i,j=q.popleft()
            for dr,dc in dir:
                rr=i+dr
                cc=j+dc
                if 0<=rr<r and 0<=cc<c and mat[rr][cc]>mat[i][j]+1:
                    mat[rr][cc]=mat[i][j]+1
                    q.append((rr,cc))
        return mat

        