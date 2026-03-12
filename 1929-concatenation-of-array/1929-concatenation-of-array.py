class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[-1]*(len(nums)*2)
        idx=0

        for i in range(len(ans)):
            if i<len(nums):
                ans[i]=nums[idx]
                idx+=1
            else:
                ans[i]=nums[i-idx]
        
        return ans
        