class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        bucket=[False]*(len(nums)+1)

        for num in nums:
            if 0<num<=len(nums):
                bucket[num]=True
        
        for i in range(1,len(nums)+1):
            if not bucket[i]:
                return i
        return len(nums)+1

        