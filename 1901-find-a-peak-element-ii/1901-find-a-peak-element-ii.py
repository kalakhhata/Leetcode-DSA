class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        lo,hi=0,len(mat[0])-1
        row,col=len(mat),len(mat[0])-1

        while lo<=hi:
            mid=lo+(hi-lo)//2
            maxi=self.getMaxRow(mat,mid,row)

            left=mat[maxi][mid-1] if mid-1>=0 else -1
            right=mat[maxi][mid+1] if mid+1<=col else -1

            if mat[maxi][mid]<left:
                hi=mid-1
            elif mat[maxi][mid]<right:
                lo=mid+1
            else:
                return [maxi,mid]
    
    def getMaxRow(self,mat,mid,row):
        maxEl=-1
        idx=-1

        for i in range(row):
            if mat[i][mid]>maxEl:
                idx=i
                maxEl=mat[i][mid]
        return idx
        