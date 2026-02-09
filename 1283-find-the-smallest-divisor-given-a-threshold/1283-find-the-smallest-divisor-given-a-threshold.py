class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)

        while low<=high:
            mid=(low+high)//2
            ans=self.canDivide(nums,threshold,mid)

            if ans:
                high=mid-1
            else:
                low=mid+1
        
        return low
    
    def canDivide(self,nums,threshold,mid):
        s=0
        for num in nums:
            s+=ceil(num/mid)
        
        return s<=threshold

        