class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        s=0

        prev=defaultdict(int)
        prev[0]=1

        for num in nums:
            s+=num
            rem=s-k
            if rem in prev:
                cnt+=prev[rem]
            prev[s]+=1
        return cnt

