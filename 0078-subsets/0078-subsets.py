class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]

        def getSubset(i):
            #base-case
            if i>=len(nums):
                res.append(subset[:])
                return
            
            #left leaf
            subset.append(nums[i])
            getSubset(i+1) 
            
            #right leaf
            subset.pop()
            getSubset(i+1)
        
        getSubset(0)
        return res
        
        