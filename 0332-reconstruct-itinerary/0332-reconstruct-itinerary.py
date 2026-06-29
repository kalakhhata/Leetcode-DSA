class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj=defaultdict(list)

        for dep,des in sorted(tickets,reverse=True):
            adj[dep].append(des)
        
        itenery=[]

        def dfs(src):

            while adj[src]:
                nxt=adj[src].pop()
                dfs(nxt)
            
            itenery.append(src)
        
        dfs('JFK')
        return itenery[::-1]