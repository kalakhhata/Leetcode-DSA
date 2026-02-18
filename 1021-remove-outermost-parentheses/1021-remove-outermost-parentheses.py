class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        cnt=0
        ans=""
        for c in s:
            if c==")":
                cnt-=1
            if cnt!=0:
                ans+=c
            if c=="(":
                cnt+=1
            
        
        return ans
            