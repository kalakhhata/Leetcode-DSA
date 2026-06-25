class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path=[False]*numCourses
        visited=[False]*numCourses
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
        st=[]

        def dfs(n):
            visited[n]=True
            path[n]=True

            for ne in adj[n]:
                if not visited[ne]:
                    if dfs(ne):
                        return True
                elif path[ne]:
                    return True
            
            path[n]=False
            st.append(n)
            return False
        

        for node in range(numCourses):
            if not visited[node]:
                if dfs(node):
                    return []
        
        return st
        