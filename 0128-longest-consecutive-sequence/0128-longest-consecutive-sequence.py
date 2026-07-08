class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket=set(nums)

        ans=0
        for num in bucket:
            x=num
            cnt=1
            if x-1 not in bucket:
                while x+1 in bucket:
                    x=x+1
                    cnt+=1
            ans=max(cnt,ans)
        
        return ans

        