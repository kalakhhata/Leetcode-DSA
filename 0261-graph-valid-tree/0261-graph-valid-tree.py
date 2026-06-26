class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        #To be a Valid Tree
        #1. It has to be undirected and there must be no loop
        #2. num of edges must be (n-1) where n is number of nodes

        visited=[False]*n
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
        def dfs(n,parent):
            visited[n]=True
            
            for ne in adj[n]:
                if not visited[ne]:
                    if not dfs(ne,n):
                        return False
                elif ne!=parent:
                    return False
            
            return True
        if not dfs(0,-1):
            return False
        
        return all(visited)
        