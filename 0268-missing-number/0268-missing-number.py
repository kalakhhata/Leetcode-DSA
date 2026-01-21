class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start=1
        temp=0
        real=0
        for i in range(len(nums)):
            temp+=start
            start+=1
            real+=nums[i]
        
        return temp-real
        