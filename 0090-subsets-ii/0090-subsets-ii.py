class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        ans=[]
        nums.sort()
        def getSubset(start):
          
            res.append(ans[:])
            
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                ans.append(nums[i])
                getSubset(i+1)
                ans.pop()
        
        getSubset(0)
        return res