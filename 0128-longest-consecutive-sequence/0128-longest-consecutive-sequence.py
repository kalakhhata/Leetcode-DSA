class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set=set(nums)
        cnt=0
        max_cnt=0
        for num in num_set:
            if num-1 not in num_set:
                temp=num
                cnt=1
                while temp+1 in num_set:
                    cnt+=1
                    temp+=1
            max_cnt=max(cnt,max_cnt)
        
        return max_cnt
        