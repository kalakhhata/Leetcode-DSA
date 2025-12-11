class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=b=c=-1
        cnt=0

        for i,ch in enumerate(s):
            if ch=='a':
                a=i
            elif ch=='b':
                b=i
            else:
                c=i
            cnt+=min(a,b,c)+1
        
        return cnt
