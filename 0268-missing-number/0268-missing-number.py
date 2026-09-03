class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op=0
        for i in range(1,len(nums)+1):
            op^=i
            op^=nums[i-1]
        return op

        
        