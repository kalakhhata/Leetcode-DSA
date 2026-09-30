class Solution:
    def rob(self, nums: list[int]) -> int:
        memo={}
        def solve(i,n):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            
            steal=nums[i] + solve(i+2,n)
            skip=solve(i+1,n)

            memo[i]=max(steal,skip)
            return max(steal,skip)
        
        return solve(0,len(nums))
        