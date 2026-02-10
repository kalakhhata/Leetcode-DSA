class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=low+(high-low)//2
            if self.canSplit(nums,mid,k):
                high=mid-1
            else:
                low=mid+1
        
        return low
    
    def canSplit(self,nums,mid,k):
        cnt=1
        temp_len=nums[0]

        for i in range(1,len(nums)):
            if temp_len+nums[i]>mid:
                cnt+=1
                temp_len=nums[i]
            else:
                temp_len+=nums[i]
        return cnt<=k
        