class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        st=[]
        adj=[[] for _ in range(numCourses)]
        visited=[False]*numCourses
        path=[False]*numCourses
        for u,v in prerequisites:
            adj[u].append(v)
        
        def dfs(node):
            visited[node]=True
            path[node]=True

            for ne in adj[node]:
                if not visited[ne]:
                    if dfs(ne):
                        return True
                elif path[ne]:
                    return True
                

            path[node]=False
            st.append(node)
            return False
        



        for node in range(numCourses):
            if not visited[node]:
                if dfs(node):
                    return []
                
        
        return st






        
        