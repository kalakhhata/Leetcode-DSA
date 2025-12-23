class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        cnt=0
        temp=0

        for r in range(len(nums)):
            if nums[r]!=1:
                temp+=1
            
            while temp>k:
                if nums[l]==0:
                    temp-=1
                l+=1
            cnt=max(cnt,r-l+1)
        return cnt