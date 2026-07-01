class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*n
        
        def dfs(node,parent):
            
            visited[node]=True

            for ne in adj[node]:
                if not visited[ne]:
                    if not dfs(ne,node):
                        return False
                elif ne!=parent:
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        
        return all(visited)
                    
            
        
        