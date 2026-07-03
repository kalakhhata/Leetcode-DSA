import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        
        adj = defaultdict(list)
        q=deque()
        q.append((src,0)) #stop,node,cost
        for u,v,price in flights:
            adj[u].append((v,price))
        minCost=[float('inf')]*n
        minCost[src]=0
        stops=0
        while q and stops <= k:

            for _ in range(len(q)):

                node, cost = q.popleft()

                for nei, price in adj[node]:

                    if cost + price < minCost[nei]:
                        minCost[nei] = cost + price
                        q.append((nei, minCost[nei]))

            stops += 1

        return -1 if minCost[dst] == float("inf") else minCost[dst]

        