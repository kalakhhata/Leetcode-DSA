class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        bucket=set()
        ans=0
        for r in range(len(s)):
            while s[r] in bucket:
                bucket.remove(s[l])
                l+=1
            bucket.add(s[r])
            ans=max(ans,r-l+1)
        
        return ans

        