class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=set()
        left=0
        ans=0

        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left+=1
            
            temp.add(s[right])
            ans=max(ans,right-left+1)
        
        return ans
