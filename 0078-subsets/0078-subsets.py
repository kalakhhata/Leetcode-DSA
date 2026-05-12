class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset=[]
        res=[]

        def getSubset(i,subset):
            if i==len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            getSubset(i+1,subset)
            subset.pop()
            getSubset(i+1,subset)
        
        getSubset(0,subset)
        return res
        
        