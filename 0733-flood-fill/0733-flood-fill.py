class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=deque()
        q.append((sr,sc))
        token=image[sr][sc]
        row=len(image)
        col=len(image[0])
        dire=[(0,1),(0,-1),(1,0),(-1,0)]

        if token==color:
            return image
        def dfs(i,j,token):
            if i<0 or i>=row or j<0 or j>=col or image[i][j]!=token:
                return 
            
            image[i][j]=color
            dfs(i+1,j,token)
            dfs(i-1,j,token)
            dfs(i,j+1,token)
            dfs(i,j-1,token)
        
        
        dfs(sr,sc,token)
        
        return image



        