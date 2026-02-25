from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        q=deque()
        q.append((sr,sc))
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        token=image[sr][sc]

        if token==color:
            return image

        while q:
            i,j=q.popleft()
            image[i][j]=color
            for r,c in dir:
                rr=i+r
                cc=j+c
                if 0<=rr<row and 0<=cc<col and image[rr][cc]==token:
                    q.append((rr,cc))
        
        return image
                        


                

        