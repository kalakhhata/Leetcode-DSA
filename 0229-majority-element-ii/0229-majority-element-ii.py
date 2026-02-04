class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1=-1
        maj2=-1
        cnt1=0
        cnt2=0
        ans=[]
        for i in range(len(nums)):
            if cnt1<=0 and maj2!=nums[i]:
                maj1=nums[i]
                cnt1=1
            elif cnt2<=0 and maj1!=nums[i]:
                maj2=nums[i]
                cnt2=1
            elif maj1==nums[i]:
                cnt1+=1
            elif maj2==nums[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1=0
        cnt2=0
        for num in nums:
            if num==maj1:
                cnt1+=1
            elif num==maj2:
                cnt2+=1
        
        if cnt1>len(nums)//3:
            ans.append(maj1)
        if cnt2>len(nums)//3:
            ans.append(maj2)
        
        return ans
        

        
        
        