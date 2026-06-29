import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj=defaultdict(list)
        minHeap=[]

        for no,d,w in times:
            adj[no].append((d,w))
        
        minHeap.append((0,k))
        visited=set()
        ans=0

        while minHeap:
            dist,node=heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)
            ans=max(ans,dist)

            for ne,weight in adj[node]:
                if ne not in visited:
                    heapq.heappush(minHeap,(weight+dist,ne))
        
        return ans if len(visited)==n else -1

        


        