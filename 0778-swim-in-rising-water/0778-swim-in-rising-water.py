import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        minH=[(grid[0][0],0,0)]
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        visited.add((0,0))

        while minH:
            t,r,c=heapq.heappop(minH)
            if r==n-1 and c==n-1:
                return t

            for dr,dc in directions:
                nei,nej=r+dr,c+dc
                if nei<0 or nej<0 or nej==n or nei==n or (nei,nej) in visited:
                    continue
                visited.add((nei,nej))
                heapq.heappush(minH,(max(t,grid[nei][nej]),nei,nej))
        
        