class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        bucket=[0]*(len(nums)+1)
        for num in nums:
            if 0<num<=len(nums):
                bucket[num]=1
        
        for i in range(1,len(nums)+1):
            if bucket[i]==0:
                return i
        
        return len(nums)+1

        
        