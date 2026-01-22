class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=None
        cnt=0
        for i in range(len(nums)):
            if cnt<=0:
                maj=nums[i]
                cnt+=1
            else:
                if maj!=nums[i]:
                    cnt-=1
                else:
                    cnt+=1
        
        return maj

