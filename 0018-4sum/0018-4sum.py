class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        if len(nums)<4:
            return []
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if s>target:
                        l-=1
                    elif s<target:
                        k+=1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                
        return ans
        
        