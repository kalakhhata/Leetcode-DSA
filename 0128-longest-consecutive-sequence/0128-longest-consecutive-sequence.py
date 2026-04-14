class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket=set(nums)
        cnt=0
        for num in bucket:
            ans=0
            n=num
            if n-1 not in bucket:
                ans+=1
                while n+1 in bucket:
                    ans+=1
                    n+=1
            cnt=max(cnt,ans)
        return cnt



        