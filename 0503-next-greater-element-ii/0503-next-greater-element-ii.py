class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(nums)
        result=[-1]*n
        n=len(nums)

        for i in range(2*n):
            while stack and nums[stack[-1]]<nums[i%n]:
                result[stack.pop()]=nums[i%n]
            if i<n:
                stack.append(i)
        
        return result