class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir=0
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        res=[]
        while top<bottom and left<right:
            if dir==0:
                for i in range(left,right):
                    res.append(matrix[top][i])
                top+=1
            elif dir==1:
                for i in range(top,bottom):
                    res.append(matrix[i][right-1])
                right-=1
            elif dir==2:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[bottom-1][i])
                bottom-=1
            elif dir==3:
                for i in range(bottom-1,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            
            dir+=1
            if dir==4:
                dir=0
            

        return res
        