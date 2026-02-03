class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        temp={}
        for i in range(len(nums)):
            if target-nums[i] in temp:
                ans[0]=i
                ans[1]=temp[target-nums[i]]
                break
            temp[nums[i]]=i
        return ans
        