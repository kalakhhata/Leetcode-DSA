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
        
        while q:
            r,c=q.popleft()
            image[r][c]=color

            for i,j in dire:
                rr=r+i
                cc=c+j
                if 0<=rr<row and 0<=cc<col and image[rr][cc]==token:
                    q.append((rr,cc))
        
        return image



        