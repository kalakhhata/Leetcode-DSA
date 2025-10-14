class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        sum=0
        prev=defaultdict(int)
        prev[0]=1 # for subarrays that starting for index 0
        for num in nums:
            sum+=num
            rem=sum-k
            if rem in prev:
                cnt+=prev[rem]
            prev[sum]+=1
        
        return cnt
        