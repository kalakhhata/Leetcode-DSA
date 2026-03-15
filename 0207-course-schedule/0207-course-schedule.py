class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[False]*numCourses
        path=[False]*numCourses
        adj=[[] for _ in range(numCourses)]
        indeg=[0]*numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indeg[u]+=1
        
        def dfs(c):
            visited[c]=True
            path[c]=True

            for neighbour in adj[c]:
                if not visited[neighbour]:
                    if not dfs(neighbour):
                        return False
                elif path[neighbour]:
                    return False
            
            path[c]=False
            return True
        
        for node in range(numCourses):
            if not visited[node]:
                if not dfs(node):
                    return False
        
        return True
               
        
        





        for c in range(numCourses):
            if not visited[c]:
                if not dfs(c,-1):
                    return False
        
        return True

        