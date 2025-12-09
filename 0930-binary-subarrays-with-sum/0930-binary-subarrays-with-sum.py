class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atMost(k):
            if k<0:
                return 0
            
            count=0
            l=0
            cumsum=0
            for r in range(len(nums)):
                cumsum+=nums[r]
                
                while cumsum>k:
                    cumsum-=nums[l]
                    l+=1
                count+=(r-l)+1
            
            return count
        
        return atMost(goal)-atMost(goal-1)