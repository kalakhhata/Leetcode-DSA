class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=len(nums)-2
        while k!=-1 and nums[k]>=nums[k+1]:
            k-=1
        
        if k!=-1:
            j=len(nums)-1
            while nums[j]<=nums[k]:
                j-=1
            nums[j],nums[k]=nums[k],nums[j]

        nums[k+1:]=nums[k+1:][::-1]
