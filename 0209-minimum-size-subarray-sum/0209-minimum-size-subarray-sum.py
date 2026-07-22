class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans=float('inf')
        left=0
        cum_sum=0


        for right in range(len(nums)):
            cum_sum+=nums[right]
            while cum_sum>=target and left<=right:
                ans=min(ans,right-left+1)
                cum_sum-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0



        