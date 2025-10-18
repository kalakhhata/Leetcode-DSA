class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=set()
        temp=[]
        nums.sort()
        def getUSubset(i,temp):
            if i==len(nums):
                ans.add(tuple(temp[:]))
                return
            
            temp.append(nums[i])
            getUSubset(i+1,temp)
            temp.pop()
            getUSubset(i+1,temp)
        
        getUSubset(0,temp)
        return [list(t) for t in ans]
        