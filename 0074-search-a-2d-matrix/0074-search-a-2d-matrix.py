class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low=0
        high=(len(matrix)*len(matrix[0]))-1

        while low<=high:
            mid=low+(high-low)//2
            temp=self.numFound(matrix,mid)
            if temp==target:
                return True
            elif temp>target:
                high=mid-1
            else:
                low=mid+1
        
        return False
    
    def numFound(self,matrix,mid):
        row=mid//len(matrix[0])
        col=mid%len(matrix[0])
        return matrix[row][col]
        