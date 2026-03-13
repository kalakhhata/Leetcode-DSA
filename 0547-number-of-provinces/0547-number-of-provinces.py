class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited=[False]*len(isConnected)
        provinces=0

        def dfs(city,isConnected):
            visited[city]=True

            
            for i in range(len(isConnected[city])):
                if isConnected[city][i]==1 and not visited[i]:
                    dfs(i,isConnected)






        for city in range(len(isConnected)):
            if not visited[city]:
                provinces+=1
                dfs(city,isConnected)
        
        return provinces

        