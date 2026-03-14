class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)

    


        for node in range(len(graph)):
            if color[node]==-1:
                if not self.check(node,graph,color):
                    return False
        return True
    
    def check(self,node,graph,color):
        q=deque([node])
        color[node]=0

        while q:
            curr = q.popleft()

            for ne in graph[curr]:
                if color[ne] == -1:
                    color[ne] = 1 - color[curr]
                    q.append(ne)

                elif color[ne] == color[curr]:
                    return False
        
        return True
        

        