class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp={}
        ans=[-1,-1]
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in temp:
                ans[0]=temp.get(rem)
                ans[1]=i
            temp[nums[i]]=i
        
        return ans
        