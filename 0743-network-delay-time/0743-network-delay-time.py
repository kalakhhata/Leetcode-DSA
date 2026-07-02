import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        minH=[]
        minH.append((0,k))
        visited=[False]*n
        adj=defaultdict(list)
        for u,v,d in times:
            adj[u].append([v,d])

        ans=0
        while minH:
            dist,node=heapq.heappop(minH)

            if visited[node-1]:
                continue
            visited[node-1]=True
            ans=max(dist,ans)
            for ne,d in adj[node]:
                if not visited[ne-1]:
                    heapq.heappush(minH,(dist+d,ne))
        
        return ans if all(visited) else -1
            
            
            




        