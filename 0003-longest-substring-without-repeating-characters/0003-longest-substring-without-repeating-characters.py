class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        ans=0
        bucket=set()

        for r in range(len(s)):
            while s[r] in bucket:
                bucket.remove(s[l])
                l+=1
            
            ans=max(ans,r-l+1)
            bucket.add(s[r])
        
        return ans