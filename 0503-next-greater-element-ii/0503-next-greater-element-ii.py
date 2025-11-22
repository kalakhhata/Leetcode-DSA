class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[]
        nge=[-1]*n

        for i in range(2*n):
            while stack and nums[stack[-1]]<nums[i%n]:
                nge[stack.pop()]=nums[i%n]
            if i<n:
                stack.append(i)
        
        return nge