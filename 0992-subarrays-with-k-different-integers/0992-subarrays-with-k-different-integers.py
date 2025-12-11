from collections import defaultdict
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(m):
            if m<=0:
                return 0
            l=0
            cnt=0
            temp=defaultdict(int)
            for r in range(len(nums)):
                temp[nums[r]]+=1
                while len(temp)>m:
                    temp[nums[l]]-=1
                    if temp[nums[l]]==0:
                        del temp[nums[l]]
                    l+=1
                cnt+=(r-l)+1
            return cnt
        
        return atMost(k)-atMost(k-1)
                


        