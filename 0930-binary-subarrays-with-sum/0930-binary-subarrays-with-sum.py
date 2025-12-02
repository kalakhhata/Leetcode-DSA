class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count={0:1}
        cum_sum=0
        count_subarr=0

        for num in nums:
            cum_sum+=num

            if cum_sum-goal in count:
                count_subarr+=count[cum_sum-goal]
            count[cum_sum]=count.get(cum_sum,0)+1
        
        return count_subarr
        