class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(i):
            if i<0:
                return 0
            count=0
            l=0
            currsum=0
            for r in range(len(nums)):
                currsum+=nums[r]%2
                
                while currsum>i:
                    currsum-=nums[l]%2
                    l+=1
                count+=(r-l)+1
            
            return count
        
        return atMost(k)-atMost(k-1)