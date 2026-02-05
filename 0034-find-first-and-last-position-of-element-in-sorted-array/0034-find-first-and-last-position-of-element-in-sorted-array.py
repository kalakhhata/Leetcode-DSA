class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=self.getTarget(0,len(nums)-1,nums,target,True)
        right=self.getTarget(0,len(nums)-1,nums,target,False)
        return [left,right]
    
   
    
    def getTarget(self,low,high,nums,target,bol):
        left=low
        right=high
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                ans=mid
                if bol:
                    right=mid-1
                else:
                    left=mid+1
        return ans
            

        