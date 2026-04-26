class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def getTarget(idx):
            low=0
            high=len(matrix[idx])-1
            while low<=high:
                mid=(low+high)//2
                if matrix[idx][mid]>target:
                    high=mid-1
                elif matrix[idx][mid]<target:
                    low=mid+1
                else:
                    return True
            return False
        for i in range(len(matrix)):
            if getTarget(i):
                return True
        return False
        