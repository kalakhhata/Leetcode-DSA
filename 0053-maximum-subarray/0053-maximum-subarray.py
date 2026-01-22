class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0
        maxsum=float('-inf')
        for i in range(len(nums)):
            summ+=nums[i]
            
            maxsum=max(summ,maxsum)
            if summ<0:
                summ=0
        
        return maxsum
            
