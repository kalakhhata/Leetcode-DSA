class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo=0 #takes care of min open parenthesis
        hi=0 #takes care of max open parenthesis

        for pt in s:
            if pt=='(':
                lo+=1
                hi+=1
            elif pt==')':
                lo=max(lo-1,0)
                hi-=1
            else:
                lo=max(lo-1,0)
                hi+=1
            if hi<0:
                return False
        
        return lo==0


        