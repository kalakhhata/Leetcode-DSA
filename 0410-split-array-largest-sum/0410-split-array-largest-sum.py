class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=low+(high-low)//2
            ans=self.canSplit(nums,k,mid)

            if ans:
                high=mid-1
            else:
                low=mid+1
        
        return low
    
    def canSplit(self,nums,k,mid):
        cnt=1
        s=nums[0]

        for i in range(1,len(nums)):
            if s+nums[i]<=mid:
                s+=nums[i]
            else:
                cnt+=1
                s=nums[i]
        
        return cnt<=k
        