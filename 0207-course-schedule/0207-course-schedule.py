class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path=[False]*numCourses
        visited=[False]*numCourses
        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
        
        def dfs(n):
            visited[n]=True
            path[n]=True

            for ne in adj[n]:
                if not visited[ne]:
                    if not dfs(ne):
                        return False
                elif path[ne]:
                    return False
            path[n]=False
            return True

        
        
        for node in range(numCourses):
            if not visited[node]:
                if not dfs(node):
                    return False
        
        return True
        