from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """



        
        
        q=deque()
        visited=set()

        def addRoom(r,c):
            if r<0 or c<0 or r>=len(rooms) or c>=len(rooms[0]) or (r,c) in visited or rooms[r][c]==-1:
                return
            
            q.append([r,c])
            visited.add((r,c))

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        dist=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                rooms[r][c]=dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist+=1
        

                    
        
        