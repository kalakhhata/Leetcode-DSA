class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                temp+=1
        
        if nums[0]>=nums[-1]:
            temp-=1
        
        return temp<1
        
        