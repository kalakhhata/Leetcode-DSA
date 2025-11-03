class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset=[]
        
        for mask in range(1<<len(nums)):
            ans=[]
            for i in range(len(nums)):
                if mask & (1<<i):
                    ans.append(nums[i])
            subset.append(ans)
        
        return subset
        
        
        