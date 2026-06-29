import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj=defaultdict(list)
        n=len(points)
        
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        
        visited=set()
        minHeap=[(0,0)] #dist,node
        ans=0
        while len(visited)<n:
            dist,node=heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited.add(node)
            ans+=dist

            for d,nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap,(d,nei))
        
        return ans
        


        