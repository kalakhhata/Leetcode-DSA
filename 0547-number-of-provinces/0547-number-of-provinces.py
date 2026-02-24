class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        isVisited=[False]*n
        province=0

        def dfs(city):
            isVisited[city]=True

            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and not isVisited[neighbour]:
                    dfs(neighbour)
        
        for city in range(n):
            if not isVisited[city]:
                dfs(city)
                province+=1
        
        return province

        