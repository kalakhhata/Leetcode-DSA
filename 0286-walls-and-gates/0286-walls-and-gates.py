class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n=len(rooms)
        m=len(rooms[0])
        q=deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    q.append((0,i,j))
        
        while q:
            for i in range(len(q)):
                d,r,c=q.popleft()
                rooms[r][c]=min(d,rooms[r][c])

                if r+1<n and rooms[r+1][c]==2147483647:
                    q.append((d+1,r+1,c))
                if r-1>=0 and rooms[r-1][c]==2147483647:
                    q.append((d+1,r-1,c))
                if c+1<m and rooms[r][c+1]==2147483647:
                    q.append((d+1,r,c+1))
                if c-1>=0 and rooms[r][c-1]==2147483647:
                    q.append((d+1,r,c-1))
        
        