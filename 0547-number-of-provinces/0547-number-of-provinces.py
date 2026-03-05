class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[False]*len(isConnected)
        provinces=0

        #explore each nodes
        def explore(node):
            visited[node]=True

            for neighbours in range(len(isConnected)):
                if not visited[neighbours] and isConnected[node][neighbours]==1:
                    explore(neighbours)

        #Check each node
        for i in range(len(isConnected)):
            if not visited[i]:
                provinces+=1
                explore(i)
        
        return provinces
        