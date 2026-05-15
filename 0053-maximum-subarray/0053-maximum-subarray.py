class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            maxSum=max(s,maxSum)
            if s<0:
                s=0
        return maxSum



            

        