class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj=[[] for _ in range(n)]
        visited=[False]*n
        ans=0

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node,p):
            visited[node]=True

            for ne in adj[node]:
                if not visited[ne]:
                    dfs(ne,node)
            


        for node in range(n):
            if not visited[node]:
                ans+=1
                dfs(node,-1)
        
        return ans
        